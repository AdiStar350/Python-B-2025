"""
add_numbers_module.py

This module provides a simple function to sum an arbitrary
number of integers and a main function to demonstrate its usage.
"""


def add(*nums: int) -> int:
	"""
	Sums an arbitrary number of integers passed as arguments.
	
	Args:
	*nums (int): A variable number of integer arguments.
	
	Returns:
	int: The total sum of all input integers.
	"""
	
	sum: int = 0
	
	for n in nums:
		sum += n
		
	return sum
	
	
def main() -> None:
	"""
	Demonstrates the usage of the 'add' function with example inputs.
	Prints the results to the console.
	"""
	
	sum_1: int = add(1, 2, 5, 2, 4, 1)
	print(sum_1)
	
	sum_2: int = add(5, sum_1)
	print(sum_2)
	
	
if __name__ == '__main__':
	main()

