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

        solution = []

        # read contents of the file
        for file in sorted(os.listdir(dir_path)):
            file_path = os.path.join(dir_path, file)
            with open(file_path) as opened_file:
                line = opened_file.readline()
                solution.append(line)

        # write contents to new file
        with open("output_file.txt", "w") as output_file:
            for num in solution:
                output_file.write(num + ', ')


read_and_write_files("/Users/jprzygoda/PYTHON-BASIC/practice/3_python_testing/tasks/files")