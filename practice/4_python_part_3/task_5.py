from typing import Tuple
from unittest.mock import Mock, patch
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     # >>> make_request('https://www.google.com')
     # 200, 'response data'
"""


def make_request(url: str) -> Tuple[int, str]:
    try:
        resp = urlopen(url)
        return resp.getcode(), resp.read().decode('utf-8')
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)
    except TimeoutError:
        print("Request timed out. Please try again.")


"""
Write test for make_request function
Use Mock for mocking request with urlopen https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 200
    >>> m.method2.return_value = b'some text'
    >>> m.method()
    200
    >>> m.method2()
    b'some text'
"""


@patch("task_5.urlopen")
def test_make_request(mocked_url):
    m = Mock()
    m.getcode.return_value = 200
    m.read.return_value = b'some text'
    mocked_url.return_value = m

    result = make_request('https://www.google.com')

    assert (result[0], result[1]) == (200, "some text")