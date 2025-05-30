# import os

# try:
#     poopoo
# except NameError as err:
#     print(err)
#     print("No poopoo here")
#     # os.system("sudo shutdown -r now") -> mac os / os.system("shutdown -r -t 00 -f") -> windows


# d = {"name" : "ricky"}

# def get(dic, key):
#     """
#     Retrieve the value associated with a given key from a dictionary.

#     Args:
#         d (dict): The dictionary to retrieve the value from.
#         key: The key whose associated value is to be retrieved.

#     Returns:
#         The value associated with the key if it exists, otherwise None.
#     """

#     try:
#         return dic[key]
#     except KeyError:
#         return None

# print(get(d, "name"))

# try:
#     num = int(float(input("Enter a number: ")))
# except ValueError:
#     print("Thats not a number you dumb cunt!")
# else:
#     print("Thank you, asshole!")
# finally:
#     print("Now go and fuck yourself.")


# while True:
#     try:
#         num = int(float(input("Enter a number: ")))
#     except ValueError:
#         print("Thats not a number you dumb cunt!")
#     else:
#         print("Thank you, asshole!")
#         break
#     finally:
#         print("Now go and fuck yourself.")

# def division(n1: int, n2: int) -> float:
#     """
#     Perform division of two integers and handle potential errors.

#     Args:
#         n1 (int): The numerator.
#         n2 (int): The denominator.

#     Returns:
#         float: The result of the division if successful.
#         None: If division by zero or invalid input occurs.

#     Exceptions:
#         ZeroDivisionError: Raised when attempting to divide by zero.
#         TypeError: Raised when inputs are not numbers.

#     Notes:
#         Prints an error message to the console if an exception occurs.
#     """
#     try:
#         res =  n1 / n2
#     except (ZeroDivisionError, TypeError):
#         print("Cant divide by zero! And both should be numbers!")
#         return 0

#     print(f"{n1} divided by {n2} is {res:.2f}")
#     return res

# def division(num1: int, num2: int) -> float:
#     """
#     Divides two numbers and returns the result.

#     Args:
#         num1 (int): The numerator.
#         num2 (int): The denominator.

#     Returns:
#         float: The result of the division if successful.

#     Raises:
#         TypeError: If the inputs are not numbers.
#         ZeroDivisionError: If an attempt is made to divide by zero.

#     Note:
#         If a TypeError occurs, a string message is returned instead of raising the exception.
#         If a ZeroDivisionError occurs, an error message is printed, and the exception is re-raised.
#     """
#     try:
#         return num1 / num2
#     except TypeError:
#         return "Please provide 2 numbers."
#     except ZeroDivisionError as exc:
#         raise ZeroDivisionError("Please do not divide by 0.") from exc

# print(division(4, 2))
# print(division([], "1"))
# print(division(1, 0))
