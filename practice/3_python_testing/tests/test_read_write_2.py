"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""

from unittest.mock import patch
import tempfile as tf
import sys
sys.path.append("..")
from tasks.task_read_write_2 import write_in_encoding


@patch("tasks.task_read_write_2.generate_words", return_value=['mujneo', 'zuxwjmh', 'ftjy', 'zpwwwojtx', 'cesiodh'])
def test_utf8_encoding(gen_words):

    # create temporary file
    _, file = tf.mkstemp(suffix=".txt", prefix="file", text=True)

    # write contents with mocked behaviour of generate words
    write_in_encoding(file, "utf-8", r"\n")

    with open(file) as f:
        output = f.readline()
        assert output == r"mujneo\nzuxwjmh\nftjy\nzpwwwojtx\ncesiodh"


@patch("tasks.task_read_write_2.generate_words", return_value=['rwliceeima', 'ghjsdymnkf', 'sjuzsjveqp', 'cesdqh',
                                                               'wsw', 'drwhezbzv', 'ijyqsclxll', 'qphpmgujf', 'okslu', 'giulu'])
def test_cp1252_encoding(gen_words):

    # create temporary file
    _, file = tf.mkstemp(suffix=".txt", prefix="file", text=True)

    # write contents with mocked behaviour of generate words
    write_in_encoding(file, "CP1252", r",")

    with open(file) as f:
        output = f.readline()
        assert output == r"rwliceeima,ghjsdymnkf,sjuzsjveqp,cesdqh,wsw,drwhezbzv,ijyqsclxll,qphpmgujf,okslu,giulu"


