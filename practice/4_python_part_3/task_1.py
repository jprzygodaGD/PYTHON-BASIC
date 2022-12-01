"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    # >>> calculate_days('2021-10-07')  # for this example today is 6 october 2021
    # -1
    # >>> calculate_days('2021-10-05')
    # 1
    # >>> calculate_days('10-07-2021')
    # WrongFormatException
"""

from datetime import datetime
import pytest


class WrongFormatException(Exception):
    pass


def calculate_days(from_date: str) -> int:

    try:
        from_date_dt = datetime.strptime(from_date, "%Y-%m-%d")
        current_date = datetime.now()
        difference = current_date - from_date_dt
        return difference.days

    except ValueError as e:
        raise WrongFormatException("Wrong format") from e


"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""
data_values = [
    ('2021-04-19', 585),
    ('2018-12-02', 1454),
    ('2022-03-14', 256),
    ('2022-11-26', -1)
]


@pytest.mark.parametrize('date, days', data_values)
def test_calculate_days_correct(date, days, freezer):
    now = datetime.now()
    assert calculate_days(date) == days


invalid_formats = [
    '10-10-2022',
    '01-31-2021',
    '05-05-2018'
]


@pytest.mark.parametrize('dates', invalid_formats)
def test_calculate_days_incorrect(dates):
    with pytest.raises(WrongFormatException):
        calculate_days(dates)



