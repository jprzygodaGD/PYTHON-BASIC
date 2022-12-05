import sys
from unittest.mock import patch, Mock
import pytest
sys.path.append("../web-venv")
from stocks import get_all_stock_symbols, get_additional_data


@pytest.fixture(scope='session')
def get_html():
    with open("../web-venv/test_stocks/page.html") as file:
        html = file.read()
    get_html = patch("stocks.get_all_stock.symbols.requests.get")
    get_html.return_value = html
    return get_html


def test_get_all_stock_symbols(get_html):

    result = get_all_stock_symbols(25)
    assert len(result) == 25
    assert result == ['NIO', 'XPEV', 'TSLA', 'AMZN', 'AAPL', 'AMD', 'ABEV', 'TLRY', 'ITUB', 'CCL', 'F', 'BAC', 'BBD',
                      'META', 'FTCH', 'NVDA', 'NU', 'CGC', 'BABA', 'AMC', 'CS', 'T', 'VALE', 'SNAP', 'INTC']


def test_get_additional_data():
    result = get_additional_data(['NIO', 'XPEV', 'TSLA'])
    assert result['NIO'][0] == 'NIO Inc.'
    assert result['XPEV'][1] == 'Guangzhou 510640'
    assert result['TSLA'][0] == 'Tesla, Inc.'

