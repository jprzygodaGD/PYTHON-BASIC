"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
import os


def read_and_write_files(dir_path):
    for file in os.listdir(dir_path):
        print(file)


read_and_write_files("/Users/jprzygoda/PYTHON-BASIC/practice/2_python_part_2/files")