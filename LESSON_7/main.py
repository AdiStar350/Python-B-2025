# """
# This module contains recursive functions:
# - n_input: Recursively prompts the user to enter numbers n times and prints each even number entered.
# - char_in_str: Checks if a character is present in a given string using recursion.
# """

# def n_input(n: int) -> None:
#     """
#     Recursively prompts the user to enter numbers n times and prints each even number entered.

#     Args:
#         n (int): The number of times to prompt the user for input.

#     Returns:
#         None
#     """
#     if n == 0:
#         return
#     num = int(input("Enter number --> "))
#     if num % 2 == 0:
#         print(num)
#     n_input(n - 1)

# n_input(6)


# def char_in_str(s: str, c: str) -> bool:
#     """
#     Checks if a character is present in a given string using recursion.

#     Args:
#         s (str): The string to search within.
#         c (str): The character to search for.

#     Returns:
#         bool: True if the character is found in the string, False otherwise.
#     """
#     if s == "":
#         return False

#     return s[0] == c or char_in_str(s[1:], c)

# print(char_in_str("hello motherfucker", "m"))


def fib(n: int) -> int:
    """
    Calculates the nth Fibonacci number using recursion.

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).

    Returns:
        int: The nth Fibonacci number.

    Examples:
        >>> fib(0)
        0
        >>> fib(1)
        1
        >>> fib(5)
        5
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(6))
