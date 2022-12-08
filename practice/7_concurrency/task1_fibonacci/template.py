import os
import datetime
from random import randint
import sys
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
sys.set_int_max_str_digits(100000000)

OUTPUT_DIR = './output'
RESULT_FILE = './output/result.csv'


def fib(n: int):
    """Calculate a value in the Fibonacci sequence by ordinal number"""

    f0, f1 = 0, 1
    for _ in range(n-1):
        f0, f1 = f1, f0 + f1
    return f1, n


def func1_helper(number: int, value: int):
    """Writes value of Fibonacci sequence to file."""

    with open(f"{OUTPUT_DIR}/file{number}.txt", "w") as opened_file:
        opened_file.write(str(value))


def func1(array: list):
    """ Calculates value of Fibonacci sequence using multiprocessing. """

    with ProcessPoolExecutor(16) as executor:
        futures = [executor.submit(fib, number) for number in array]
        for future in as_completed(futures):
            value, number = future.result()
            func1_helper(number, value)


def func2_helper(file):
    """ Reads file contents. """
    ordinal_num = file.split('.')[0].split('e')[1]
    file_path = os.path.join(OUTPUT_DIR, file)
    with open(file_path) as opened_file:
        line = opened_file.readline()
        to_write = ordinal_num + ',' + line + '\n'
        return to_write


def func2(result_file: str):
    """ Writes contents to the resul file. """

    with ThreadPoolExecutor() as executor:
        with open(result_file, "w") as result_file:
            futures = [executor.submit(func2_helper, file) for file in sorted(os.listdir(OUTPUT_DIR))]
            for future in as_completed(futures):
                text = future.result()
                result_file.write(text)


if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # It took around 40 seconds to complete without any concurrency techniques
    start = datetime.datetime.now()
    func1(array=[randint(1000, 100000) for _ in range(1000)])
    func2(result_file=RESULT_FILE)
    end = datetime.datetime.now() - start
    print(end)
