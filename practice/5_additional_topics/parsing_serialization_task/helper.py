""" Helper functions to calculate staticts for country. """


class NoSuchStatisticException(Exception):
    pass


def iterate_dict_mean(dictionary: dict, stats: str):
    """Finds mean value."""

    stats_val, num_val = 0, 0
    for label, data in dictionary.items():
        try:
            stats_val += data[stats]
            num_val += 1
        except KeyError:
            raise NoSuchStatisticException
    return stats_val, num_val


def iterate_dict_min_max(dictionary: dict, stats: str, operator, edge_val):
    """ Finds min or max value."""

    city = ''
    for label, data in dictionary.items():
        try:
            if eval(f"{data[stats]} {operator} {edge_val}"):
                city = label
                edge_val = data[stats]
        except KeyError:
            raise NoSuchStatisticException
    return city


def filter_data(cities: dict):
    """ Filter data to gather only what is needed for calculations."""

    cities_filtered = {}

    for city in cities:
        attributes = {}
        temperatures = []
        wind_speed = []
        for data in cities[city]['hourly']:
            temperatures.append(data['temp'])
            wind_speed.append(data['wind_speed'])

        attributes['temp'] = temperatures
        attributes['wind'] = wind_speed
        cities_filtered[city.replace(' ', '_')] = attributes

    return cities_filtered