"""
Create virtual environment and install Faker package only for this venv.
Write command line tool which will receive int as a first argument and one or more named arguments
 and generates defined number of dicts separated by new line.
Exec format:
`$python task_4.py NUMBER --FIELD=PROVIDER [--FIELD=PROVIDER...]`
where:
NUMBER - positive number of generated instances
FIELD - key used in generated dict
PROVIDER - name of Faker provider
Example:
`$python task_4.py 2 --fake-address=address --some_name=name`
{"some_name": "Chad Baird", "fake-address": "62323 Hobbs Green\nMaryshire, WY 48636"}
{"some_name": "Courtney Duncan", "fake-address": "8107 Nicole Orchard Suite 762\nJosephchester, WI 05981"}
"""

# TODO Add double dashes

import argparse
from faker import Faker
from unittest.mock import Mock
import test_task_4
import sys


class NoFakerModuleException(Exception):
    pass


# creating namespace
def collect_args():
    parser = argparse.ArgumentParser(description="Generate fake data")
    parser.add_argument("number")
    for arg in sys.argv[2:]:
        parser.add_argument(arg.split("=")[0])
    return parser.parse_args()


def prepare_namespace(args: argparse.Namespace) -> (dict, int):

    # unpack namespace
    namespace_dict = vars(args)

    for key, val in namespace_dict.items():
        if key != "number":
            namespace_dict[key] = val.split("=")[1]

    # prepare fields needed to generate data
    num_of_dicts = int(namespace_dict["number"])
    del namespace_dict["number"]

    return namespace_dict, num_of_dicts


def print_name_address(args: argparse.Namespace) -> None:

    fake = Faker()
    namespace_dict, num_of_dicts = prepare_namespace(args)

    # generate fake data
    for i in range(num_of_dicts):
        fake_dict = {}
        for key, val in namespace_dict.items():
            try:
                fake_val = eval(f"fake.{val}()")
                fake_dict[key] = fake_val
            except AttributeError:
                raise NoFakerModuleException
        print(fake_dict)


if __name__ == "__main__":
    arguments = collect_args()
    print_name_address(arguments)