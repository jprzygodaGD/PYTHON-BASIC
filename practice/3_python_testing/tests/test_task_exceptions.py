"""
Write tests for division() function in 2_python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""

import pytest
import sys
sys.path.append("..")
from tasks.task_exceptions import division, DivisionByOneException


test_cases1 = [
    (2, 2, 1),
    (4, 5, 0),
    (9, 2, 4)
]


@pytest.mark.parametrize("x, y, result", test_cases1)
def test_division_ok(x, y, result, capfd):
    out1 = division(x, y)
    out2, err = capfd.readouterr()
    assert out1 == result
    assert out2 == "Division finished\n"


def test_division_by_zero(capfd):
    division(2, 0)
    out, err = capfd.readouterr()
    assert out == "Division by 0\nDivision finished\n"


test_cases2 = [
    (2, 1),
    (10, 1),
    (46, 1)
]


@pytest.mark.parametrize("x, y", test_cases2)
def test_division_by_one(x, y, capfd):
    with pytest.raises(DivisionByOneException):
        division(x, y)
        out, err = capfd.readouterr()
        assert out == "Division finished\n"
