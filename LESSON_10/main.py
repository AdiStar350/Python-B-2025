"""
This module manages a list of students, sorts them by their last names, and prints the sorted list.
"""

students: list[str] = ["Mike Johnson", "Anna Smith", "John Doe", "Sara Brown", "David Wilson"]

# sorted_students: list[str] = sorted(students, key=lambda name: name.split()[-1].title())
students.sort(key=lambda name: name.split(" ")[-1].lower())

# print(sorted_students)
# print(students)


def calc_total(price: float, quantity: int, discount: float=0) -> float:
    """
    Calculates the total cost after applying a discount.

    Args:
        price (float): The price of a single item.
        quantity (int): The number of items being purchased.
        discount (float, optional): The discount rate to apply, represented as a 
            decimal (e.g., 0.1 for 10% discount). Defaults to 0.

    Returns:
        float: The total cost after applying the discount.
    """

    return price * quantity * (1 - discount)


# print(calc_total(20.00, 5, 0.25))


def add(*numbers: int) -> int:
    """
    Adds an arbitrary number of integers and returns their sum.

    Args:
        *numbers (int): A variable number of integer arguments to be summed.

    Returns:
        int: The total sum of the provided integers.
    """

    total: int = 0

    for n in numbers:
        total += n

    return total


# print(add(1, 2, 3, 4, 5))


def demo(*args: int, **kwargs: int) -> None:
    """
    Demonstrates the use of variable-length positional and keyword arguments.

    Args:
        *args (int): Variable-length positional arguments, each expected to be an integer.
        **kwargs (dict[str, int]): Variable-length keyword arguments, where each key is a string
            and each value is an integer.

    Returns:
        None
    """

    print(f"Positional: {args}")
    print(f"Keyword: {kwargs}")


# demo(1, 2, 3, 4, 5, a=5, b=8, c=7)
