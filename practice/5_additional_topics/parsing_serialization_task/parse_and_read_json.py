""" Collect data from json files. """
import json
import os
from helper import filter_data, iterate_dict_mean, iterate_dict_min_max


def read_files_from_dir(dir_path):
    """ Read files from source_data directory."""

    cities = {}

    for city in sorted(os.listdir(dir_path)):
        path_to_city_folder = os.path.join(dir_path, city)
        for json_file in os.listdir(path_to_city_folder):
            file_path = os.path.join(path_to_city_folder, json_file)
            with open(file_path) as opened_json:
                loaded_json = json.load(opened_json)
                cities[city] = loaded_json

    return cities


def calculate_city_stats(cities: dict):
    """ Calculate temperature and wind statistics for each city."""

    cities_stats = {}
    cities_filtered = filter_data(cities)

    for city, data in cities_filtered.items():

        stats = {}

        # temperature data
        stats['min_temp'] = min(data['temp'])
        stats['max_temp']= max(data['temp'])
        stats['mean_temp'] = sum(data['temp']) / len(data['temp'])

        # wind data
        stats['min_wind_speed'] = min(data['wind'])
        stats['max_wind_speed'] = max(data['wind'])
        stats['mean_wind_speed'] = sum(data['wind']) / len(data['wind'])

        cities_stats[city] = stats

    return cities_stats


def calculate_country_stats(cities: dict):
    """ Calculate temperature and wind statistics for the whole country."""

    country = {}

    # Mean temperature
    mean_temp, num_val = iterate_dict_mean(cities, 'mean_temp')
    country['mean_temp'] = mean_temp / num_val

    # Mean wind speed
    mean_wind_speed, num_val = iterate_dict_mean(cities, 'mean_wind_speed')
    country['mean_wind_speed'] = mean_wind_speed / num_val

    country['coldest_place'] = iterate_dict_min_max(cities, 'mean_temp', '<', 100)
    country['warmest_place'] = iterate_dict_min_max(cities, 'mean_temp', '>', 0)
    country['windiest_place'] = iterate_dict_min_max(cities, 'mean_wind_speed', '>', 0)

    return country


