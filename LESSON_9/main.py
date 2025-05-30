"""
This module contains a function to describe the type of a given value.

    Functions:
        describe_type(value: object) -> str:
            Possible return values include:
            - "its an int" for integers
            - "its a string" for strings
            - "its a list" for lists
"""

from datetime import datetime, date, time, timedelta

def describe_type(value: object) -> str:
    """
    Returns a string describing the type of the given value.

    Args:
        value (object): The value whose type is to be described.

    Returns:
        str: A description of the type of the value. Possible return values are:
            - "its an int" if the value is an integer
            - "its a string" if the value is a string
            - "its a list" if the value is a list
            - "something else" for any other type
    """

    match value:
        case int():
            return "its an int"
        case str():
            return "its a string"
        case list():  
            return "its a list"
        case _:
            return "something else"


def get_even_numbers(numbers: list[int]) -> list[int]:
    """
    Filters and returns a list of even numbers from the given list.

    Args:
        numbers (list[int]): A list of integers to filter.

    Returns:
        list[int]: A list containing only the even integers from the input list.

    Raises:
        AssertionError: If the resulting list contains any odd numbers.
    """

    result = [n for n in numbers if n % 2 == 0]
    assert all(n % 2 == 0 for n in numbers), "I said all numbers must be even"
    return result

date = date(2025, 5, 30)
print(f"Date: {date}")

time = time(10, 22, 30)
print(f"Time: {time}")

dt = datetime(2025, 5, 30, 10, 22, 30)
print(f"Datetime: {dt}")

now = datetime.now()
print(f"Current Datetime: {now}")

one_day = timedelta(days=1)
yesterday = now - one_day
print(f"Yesterday's Datetime: {yesterday}")

tomorrow = now + one_day
print(f"Tomorrow's Datetime: {tomorrow}")

DATE_STR = "30-07-2025 10:27:56"
dt_now = datetime.strptime(DATE_STR, "%d-%m-%Y %H:%M:%S")
print(dt_now)
israel_time = dt_now.strftime("%d-%m-%Y %H:%M:%S")
print(f"Israel Time: {israel_time}")
