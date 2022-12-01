import xml.etree.ElementTree as ET
from parse_and_read_json import read_files_from_dir, calculate_city_stats, calculate_country_stats

if __name__ == "__main__":

    # Read data
    data = read_files_from_dir('/Users/jprzygoda/PYTHON-BASIC/practice/5_additional_topics/'
                               'parsing_serialization_task/source_data')
    cities = calculate_city_stats(data)
    countries = calculate_country_stats(cities)

    # Create an XML file
    root = ET.Element('weather', country='Spain', date='2021-09-25')
    summary = ET.SubElement(root, 'summary', mean_temp=str(round(countries['mean_temp'], 2)),
                            mean_wind_speed=str(round(countries['mean_wind_speed'], 2)),
                            coldest_place=countries['coldest_place'], warmest_place=countries['warmest_place'],
                            windiest_place=countries['windiest_place'])
    cities_ele = ET.SubElement(root, 'cities')

    # Add city data
    for city, data in cities.items():
        ET.SubElement(cities_ele, city, mean_temp=str(round(data['mean_temp'], 2)),
                      mean_wind_speed=str(round(data['mean_wind_speed'], 2)), min_temp=str(round(data['min_temp'], 2)),
                      min_wind_speed=str(round(data['min_wind_speed'], 2)), max_temp=str(round(data['max_temp'], 2)),
                      max_wind_speed=str(round(data['max_wind_speed'], 2)))

    tree = ET.ElementTree(root)
    ET.indent(tree, space="\t", level=0)
    tree.write('spain_data.xml', encoding="utf-8")
