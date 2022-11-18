"""
Write function which updates dictionary with defined values but only if new value more then in dict
Restriction: do not use .update() method of dictionary
Examples:
    >>> set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)
    {'a': 1, 'b': 4, 'c': 3}
    >>> set_to_dict({}, a=0)
    {'a': 0}
    >>> set_to_dict({'a': 5})
    {'a': 5}
"""

from typing import Dict


def set_to_dict(dict_to_update: Dict[str, int], **items_to_set) -> Dict:
    """ Update value for given key only if the given value is greater than current one."""

    for key, val in items_to_set.items():
        # if key is not in dict then add it immediately
        if key not in dict_to_update:
            dict_to_update[key] = val
        # check if value for an existing key is bigger
        elif key in dict_to_update and val > dict_to_update[key]:
            dict_to_update[key] = val

    return dict_to_update
