"""
Write function which reads a number from input nth times.
If an entered value isn't a number, ignore it.
After all inputs are entered, calculate an average entered number.
Return string with following format:
If average exists, return: "Avg: X", where X is avg value which rounded to 2 places after the decimal
If it doesn't exist, return: "No numbers entered"
Examples:
    user enters: 1, 2, hello, 2, world
    >>> read_numbers(5)
    Avg: 1.67
    ------------
    user enters: hello, world, foo, bar, baz
    >>> read_numbers(5)
    No numbers entered

"""


def read_numbers(n: int) -> str:
    """Prompts for number n times and returns average."""

    numbers = []

    for i in range(n):
        try:
            num = int(input("Please enter a number: "))
        except ValueError:
            continue
        else:
            numbers.append(num)

    # calculate average if numbers were entered
    if len(numbers) == 0:
        return "No numbers entered"
    else:
        avg = sum(numbers) / len(numbers)
        return f"Avg: {avg:.2f}"

