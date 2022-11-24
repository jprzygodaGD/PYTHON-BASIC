"""
Write tests for a read_numbers function.
It should check successful and failed cases
for example:
Test if user inputs: 1, 2, 3, 4
Test if user inputs: 1, 2, Text

Tip: for passing custom values to the input() function
Use unittest.mock patch function
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

TIP: for testing builtin input() function create another function which return input() and mock returned value
"""
from unittest.mock import patch
import pytest


def custom_input():
    return input()


def read_numbers():
    solution = []

    for i in range(5):
        read = custom_input()
        if read.isdigit():
            solution.append(int(read))
        else:
            raise ValueError("Input only integers")

    return solution


@patch("test_task_input_output.custom_input", side_effect=["1", "22", "45", "23", "17"])
def test_read_numbers_without_text_input(custom_input_correct):
    assert read_numbers() == [1, 22, 45, 23, 17]


@patch("test_task_input_output.custom_input", side_effect=["1", "2", "Text"])
def test_read_numbers_with_text_input(custom_input_incorrect):
    with pytest.raises(ValueError):
        read_numbers()

