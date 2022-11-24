"""
Write function which receives filename and reads file line by line and returns min and mix integer from file.
Restriction: filename always valid, each line of file contains valid integer value
Examples:
    # file contains following lines:
        10
        -2
        0
        34
    #>>> get_min_max('filename')
    (-2, 34)

Hint:
To read file line-by-line you can use this:
with open(filename) as opened_file:
    for line in opened_file:
        ...
"""

from typing import Tuple


def get_min_max(filename: str) -> Tuple[int, int]:
    """Read integers from the file to find min and max values."""

    with open(filename) as opened_file:
        # readlines reads all lines from a file and saves them as list
        values = opened_file.readlines()

    # Cast numbers as integers
    solution = [int(num) for num in values]

    return min(solution), max(solution)


print(get_min_max("numbers.txt"))
