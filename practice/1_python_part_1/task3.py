"""
Write function which receives list of text lines (which is space separated words) and word number.
It should enumerate unique words from each line and then build string from all words of given number.
Restriction: word_number >= 0
Examples:
    >>> build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1)
    'b 2 dog'
    >>> build_from_unique_words('a b c', '', 'cat dog milk', word_number=0)
    'a cat'
    >>> build_from_unique_words('1 2', '1 2 3', word_number=10)
    ''
    >>> build_from_unique_words(word_number=10)
    ''
"""
from typing import Iterable


def build_from_unique_words(*lines: Iterable[str], word_number: int) -> str:
    """ Construct string of unique letters where enumeration matches given word_number."""

    solution = ""
    for line in lines:
        line_list = str(line).split()
        line_list_uniq = []

        # find unique items in right order
        for item in line_list:
            if item not in line_list_uniq:
                line_list_uniq.append(item)

        for num, item in enumerate(line_list_uniq):
            if num == word_number:
                # add item to the solution
                solution += item
                solution += ' '

    return solution.strip()


