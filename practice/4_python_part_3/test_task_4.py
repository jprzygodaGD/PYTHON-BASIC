import argparse
import pytest
from faker import Faker
from unittest.mock import Mock, MagicMock, patch
from task_4 import prepare_namespace, print_name_address, NoFakerModuleException
import sys


def test_prepare_namespace():
    mock = Mock(return_value=argparse.Namespace(number='2', fake_address='fake_address=address',
                                                fake_name='fake_name=name'))
    expected_output = {'fake_address': 'address', 'fake_name': 'name'}, 2
    assert prepare_namespace(mock()) == expected_output


def test_print_name_address_invalid():
    mock = Mock(return_value=argparse.Namespace(number='1', fake_name='fake_name=fake_name'))
    with pytest.raises(NoFakerModuleException):
        print_name_address(mock())


def test_print_name_address_valid(capfd):
    mock = MagicMock()
    mock.method1.return_value = argparse.Namespace(number='1', fake_address='fake_address=address',
                                                   fake_name='fake_name=name')

    print_name_address(mock.method1())
    out, err = capfd.readouterr()

    assert 'fake_address' in out
    assert 'fake_name' in out


