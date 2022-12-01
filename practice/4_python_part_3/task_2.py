"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exist, raise OperationNotFoundException
Examples:
    # >>> math_calculate('log', 1024, 2)
    # 10.0
    # >>> math_calculate('ceil', 10.7)
    # 11
"""
import math

import pytest


class OperationNotFoundException(Exception):
    pass


def math_calculate(function: str, *args):

    try:
        return eval(f"math.{function}{args}")

    except AttributeError as e:
        raise OperationNotFoundException from e



"""
Write tests for math_calculate function
"""
test_cases_a = [
    ('ceil', 10.7, 11),
    ('floor', 9.2, 9),
    ('sqrt', 100, 10)
]


@pytest.mark.parametrize('operation, a, result', test_cases_a)
def test_math_calculate_correct_a(operation, a, result):
    assert math_calculate(operation, a) == result


test_cases_b = [
    ('pow', 10, 2, 100),
    ('log', 1024, 2, 10.0),
    ('fmod', 20, 3, 2.0)
]


@pytest.mark.parametrize('operation, a, b, result', test_cases_b)
def test_math_calculate_correct_b(operation, a, b, result):
    assert math_calculate(operation, a, b) == result


test_cases_c = [
    ('sum', 2, 5),
    ('subtract', 10, 8),
    ('multiplication', 2, 2)
]


@pytest.mark.parametrize('operation, a, b', test_cases_c)
def test_math_calculate_incorrect(operation, a, b):
    with pytest.raises(OperationNotFoundException):
        math_calculate(operation, a, b)

