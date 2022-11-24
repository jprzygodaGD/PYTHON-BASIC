"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import tempfile as tf
import sys
sys.path.append("..")
from tasks.task_read_write import read_and_write_files

# TODO back to improve this one
"""Create few temp files each containing one number."""


def generate_data():

    # create temp directory where the files will be stored
    temp_dir = tf.mkdtemp()

    file1 = tf.mkstemp(suffix=".txt", prefix="file_1", dir=temp_dir, text=True)
    file2 = tf.mkstemp(suffix=".txt", prefix="file_2", dir=temp_dir, text=True)
    file3 = tf.mkstemp(suffix=".txt", prefix="file_3", dir=temp_dir, text=True)

    # write data into files
    with open(file1[1], mode="w") as f1:
        f1.write("2")

    with open(file2[1], mode="w") as f2:
        f2.write("100")

    with open(file3[1], mode="w") as f3:
        f3.write("3")

    return temp_dir


def test_read_files():
    path_to_data = generate_data()
    read_and_write_files(path_to_data)

    with open("output_file.txt") as opened_file:
        contents = opened_file.readline()

    assert contents == "2, 100, 3, "


