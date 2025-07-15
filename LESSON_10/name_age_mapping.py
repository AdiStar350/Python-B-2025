"""
name_age_mapping.py

This module provides a simple function to return
a dictionary mappinga person's name to their age.
"""


def get_names(name: str, age: int) -> dict[str, int]:
	"""
	Returns a dictionary containing a single entry mapping
	the given name to the given age.
	
	Args:
	name (str): The person's full name.
	age (int): The person's age.
	
	Returns:
	dict[str, int]: A dictionary with one key-value pair {name: age}.
	"""
	
	return {name: age}
	
	
def main() -> None:
	"""
	Demonstrates the usage of the get_names function
	by printing a sample dictionary with a hardcoded name and age.
	"""
	
	print(get_names(name="Eyal Golan's girlfriend", age=2))
	
	
if __name__ == '__main__':
	main()

