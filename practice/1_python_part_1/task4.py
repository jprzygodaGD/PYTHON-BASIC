"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value, and it's power. For first value subtract nothing.
Restriction:
Examples: because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]

"""
from typing import List


def calculate_power_with_difference(ints: List[int]) -> List[int]:
    """Calculates power of each integer and then subtracts difference between previous value and its power"""

    # Start at the second number of the list
    i = 1
    new_ints = [ints[0] ** 2]
    while i < len(ints):

        new_val = ints[i]**2 - (new_ints[i-1] - ints[i-1])
        new_ints.append(new_val)
        i += 1

    return new_ints

