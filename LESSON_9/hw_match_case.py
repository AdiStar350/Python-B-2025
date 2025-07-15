"""
hw_match_case.py

Functions:
	- type_of_character:
		Takes a string as an argument and returns it's classification as a string  by using match - case block.
		
	- main:
		Tests the type_of_character function with user input.
"""


def type_of_character(c: str) -> str:
	"""
    Determines the type of a single character.

    Args:
        c (str): The character to classify. Must be a single character string.

    Returns:
        str: A message indicating whether the character is:
             - "A Vowel"
             - "A Consonant"
             - "A Digit"
             - "A Symbol"

    Raises:
        ValueError: If the input string does not consist of exactly one character.
    """

	if len(c) != 1:
		raise ValueError("Enter just one character.")
		
	c_copy = c.lower()
	
	match c_copy:
		case _ if c_copy in ("a", "e", "i", "o", "u"):
			return "A Vowel"
		case _ if c_copy.isalpha():
			return "A Consonant"
		case _ if c_copy.isdigit():
			return "A Digit"
		case _:
			return "A Symbol"
			
			
def main() -> None:
	"""
    Main function to test type_of_character function with user input.
    """
	character = input("Enter a character: ")
	print(type_of_character(character))
	

if __name__ == "__main__":
	main()

