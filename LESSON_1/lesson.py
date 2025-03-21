"""
Lesson 1

Functions:
    validate(a: int) -> str
    is_odd(n: int) -> str
    neg_or_pos(n: int) -> str
    is_vowel(c: str) -> str
"""

# age = int(input("what is your age? "))
# num = int(input("Enter a number: "))
char = input("Enter a character: ")


def validate(a):
    """
    Determines if a person is allowed to enter based on their age.

    Args:
        age (int): The age of the person.

    Returns:
        str: A message indicating whether the person may enter or should go back.
    """
    return "you may enter" if a >= 18 else "go back to mommy"


def is_odd(n):
    """
    Check if a number is odd.

    Parameters:
    n (int): The number to check.

    Returns:
    str: "odd" if the number is odd, "not odd" otherwise.
    """
    return "odd" if n % 2 == 0 else "not odd"


def neg_or_pos(n):
    """
    Determine if a number is negative, positive, or zero.

    Args:
        n (int or float): The number to be evaluated.

    Returns:
        str: A string indicating whether the number is "negative", "positive", or "zero".
    """
    return "negative" if n < 0 else ("positive" if n > 0 else "zero")


def is_vowel(c):
    """
    Determine if a given character is a vowel or a consonant.

    Args:
        c (str): A single character to be checked.

    Returns:
        str: "vowel" if the character is a vowel, otherwise "consonant".
    """
    return "vowel" if c.lower() in "aeiou" else "consonant"


# print(validate(age))
# print(is_odd(num))
# print(neg_or_pos(num))
print(is_vowel(char))
