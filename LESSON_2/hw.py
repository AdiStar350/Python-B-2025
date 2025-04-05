"""
This script takes a list of numbers to:
    1. Separate the numbers into even and odd lists.
    2. Create a boolean list indicating if each number is even.
"""

nums = [17, 46, 28, 78, 64, 3]
even, odd = [n for n in nums if n % 2 == 0], [n for n in nums if n % 2 != 0]

# print(even)
# print(odd)

# -----------------------------------------------------------------------------------------------

even_or_not = [n % 2 == 0 for n in nums]

# print(even_or_not)
