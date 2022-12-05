from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from tabulate import tabulate
"""Scrape stock data and prepare spreadsheets."""


def get_all_stock_symbols(number_of_results):
    """ Loops through all pages of currently most active stock to extract their symbol."""

    number_of_stocks = 0
    stocks_list = []
    offset = 0
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                             'Version/15.6.1 Safari/605.1.15'}

    # Loop through all the pages
    while number_of_stocks != number_of_results:
        url_single_page = f'https://finance.yahoo.com/most-active?count=25&offset={offset}'
        single_page = requests.get(url_single_page, headers=headers).text
        single_page_html = BeautifulSoup(single_page, 'html.parser')
        single_page_div = single_page_html.find('div', id='app')
        stocks = single_page_div.find("tbody")

        for stock in stocks:
            stock_symbol = stock.find("a", {'data-test': 'quoteLink'}).text
            stocks_list.append(stock_symbol)
            number_of_stocks += 1

        offset += 25

    return stocks_list


def get_executives(symbols):
    """ Scrape data about company's executives from Profile page."""

    executives_data_final = {}

    for stock_sym in symbols:
        stock_profile_url = f'https://finance.yahoo.com/quote/{stock_sym}/profile?p={stock_sym}'
        stock_profile = requests.get(stock_profile_url, headers=headers).text
        stock_profile_html = BeautifulSoup(stock_profile, 'html.parser')
        table_ceo = stock_profile_html.find('tbody')

        executives_data_temp = []
        for record in table_ceo.find_all('tr'):
            if record is None:
                continue

            title = record.find('td', class_="Ta(start) W(45%)")
            if bool(re.search('CEO|Chief Exec|Chairman', str(title), re.IGNORECASE)):
                name = record.find_all('td')[0].text
                executives_data_temp.append(name)
                year = record.find_all('td')[-1].text
                if year == 'N/A':
                    year = 0
                executives_data_temp.append(year)

        executives_data_final[stock_sym] = executives_data_temp[:2]

    return executives_data_final


def get_additional_data(symbols):
    """Scrapes company name, country and number of employees from Profile page."""

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                             'Version/15.6.1 Safari/605.1.15'}

    additional_stock_data = {}

    for stock_sym in symbols:
        stock_profile_url = f'https://finance.yahoo.com/quote/{stock_sym}/profile?p={stock_sym}'
        stock_profile = requests.get(stock_profile_url, headers=headers).text
        stock_profile_html = BeautifulSoup(stock_profile, 'html.parser')
        container = stock_profile_html.find("div", class_="asset-profile-container")

        single_stock_data = []

        name = container.find("h3").text
        single_stock_data.append(name)
        location = str(container.find("p")).replace("<br/>", "\n").splitlines()[2]
        single_stock_data.append(location)
        num_employees = container.find_all("span")[-1].text
        single_stock_data.append(num_employees)

        additional_stock_data[stock_sym] = single_stock_data

    return additional_stock_data


def get_52_change_stats(symbols):
    """Finds data with 52 week change"""

    statistics_data_final = {}

    for symbol in symbols:
        url_stats = f'https://finance.yahoo.com/quote/{symbol}/key-statistics?p={symbol}'
        page = requests.get(url_stats, headers=headers).text
        page_html = BeautifulSoup(page, 'html.parser')

        single_stock_data = []

        name = page_html.find("h1").text
        single_stock_data.append(name.split("(")[0].rstrip())
        change = page_html.find('span', string='52-Week Change').find_parent("td").find_next_sibling().text.strip("%")
        if change == 'N/A':
            change = 0
        single_stock_data.append(change)
        total_cash = page_html.find('span', string='Total Cash').find_parent("td").find_next_sibling().text
        single_stock_data.append(total_cash)

        statistics_data_final[symbol] = single_stock_data

    return statistics_data_final


def get_blackrock_holders():
    """Scrapes holders data for BlackRock Inc. """

    url = 'https://finance.yahoo.com/quote/BLK/holders?p=BLK'
    page = requests.get(url, headers=headers).text
    html = BeautifulSoup(page, 'html.parser')

    holder_all = {}

    holders = html.find_all('table')
    institutional_holders, mutual_holders = holders[1], holders[2]

    for i_holder in institutional_holders.find_all("tr")[1:]:
        i_holder_cols = []
        for data in i_holder.find_all("td"):
            i_holder_cols.append(data.text)

        holder_all[i_holder_cols[0]] = i_holder_cols[1:]

    for m_holder in mutual_holders.find_all("tr")[1:]:
        m_holder_cols = []
        for data in m_holder.find_all("td"):
            m_holder_cols.append(data.text)

        holder_all[m_holder_cols[0]] = m_holder_cols[1:]

    return holder_all


def transform_to_dataframe(dictionary: dict, columns: list):
    """Transform scraped data to Pandas DataFrame."""

    df_temp = pd.DataFrame(data=dictionary.items(), columns=['company', 'attributes'])
    result = pd.DataFrame(df_temp["attributes"].to_list(), columns=columns)
    result['Stock'] = df_temp['company']

    return result


def print_sheet(title: str, data):
    """Prints data in tabular format."""

    header = title.center(120, "=")
    print(header)
    print(tabulate(data, headers=data.columns, tablefmt='psql'))
    print("\n")


if __name__ == "__main__":

    url = 'https://finance.yahoo.com/most-active'

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                             'Version/15.6.1 Safari/605.1.15'}
    page = requests.get(url, headers=headers, timeout=10).text
    html = BeautifulSoup(page, 'html.parser')
    main_div = html.find('div', id='app')

    # Sheet 1 - BlackRock Inc. holders
    blackrock = get_blackrock_holders()
    blackrock_df = transform_to_dataframe(blackrock, columns=['Shares', 'Date Reported', '% Out', 'Value'])
    blackrock_df.rename(columns={'Stock': 'Holder'}, inplace=True)
    blackrock_df['% Out'] = blackrock_df['% Out'].str.rstrip('%').astype('float')
    blackrock_df.sort_values(by='% Out', ascending=False, inplace=True)
    final_blackrock = blackrock_df.head(10)
    print_sheet("10 largest holds of Blackrock Inc", final_blackrock)

    try:
        # Find through how many results we have to go through
        current_number_of_results = int(main_div.findChild('span', class_="Mstart(15px) Fw(500) Fz(s)").text.split(" ")[-2])
        stock_symbols = get_all_stock_symbols(current_number_of_results)
        executives = get_executives(stock_symbols)

        # Sheet 2 - find youngest CEO's
        ceo_df = transform_to_dataframe(executives, ['CEO', 'Year Born'])
        ceo_df['Year Born'] = ceo_df['Year Born'].astype('int')
        ceo_df.sort_values(by='Year Born', ascending=False, inplace=True)
        youngest_ceo_df = ceo_df.head(5)

        add_data = get_additional_data(list(ceo_df.Stock.head(5)))
        add_data_df = transform_to_dataframe(add_data, ['Name', 'Location', 'Employees'])
        final_df_youngest_ceo = youngest_ceo_df.merge(add_data_df, on='Stock')
        print_sheet("5 stocks with most youngest CEOs", final_df_youngest_ceo)

        # Sheet 3 - 52 week change
        week_change = get_52_change_stats(stock_symbols)
        week_change_df = transform_to_dataframe(week_change, ['Name', '52 Change (%)', 'Total Cash'])
        week_change_df['52 Change (%)'] = week_change_df['52 Change (%)'].astype('float')
        week_change_df.sort_values(by='52 Change (%)', ascending=False, inplace=True)
        final_df_52_change = week_change_df.head(10)
        print_sheet("10 stocks with best 52-Week Change", final_df_52_change)

    except AttributeError:
        print("Website not available. Please try again")
