"""
hw_datetime.py

This script calculates the current time in Japan 13 days from a given input time (in HH:MM format).

Functions:
	- japan_time_in_13_days(t: str) -> str:
		Converts input time to the equivalent time 13 days later in Japan.
	- main() -> None:
		Handles user input and displays the result.
"""

from datetime import datetime, timedelta


def japan_time_in_13_days(t: str) -> str:
	"""
	Given a time string in HH:MM format, calculates the datetime 13 days later 
	from today at that time, and returns it formatted as a Japanese datetime string.

	Args:
		t (str): A time string in the format "HH:MM".

	Returns:
		str: A string representing the datetime 13 days from today at the input time,
		formatted as "YYYY年MM月DD日 HH時MM分SS秒".

	Raises:
		ValueError: If the input time format is invalid.
	"""

	try:
		time_part = datetime.strptime(t, "%H:%M").time()
		full_datetime = datetime.combine(datetime.now().date(), time_part)
		day_gap = timedelta(days=13)
		
		full_datetime += day_gap
	
		return full_datetime.strftime("%Y年%m月%d日 %H時%M分%S秒")
	
	except ValueError:
		raise ValueError("Invalid time format. Use HH:MM.")


def main() -> None:
	"""
	Main function to execute the program.
	Prompts the user for input and prints the computed Japanese datetime.
	"""

	time_input = input("Enter time (HH:MM): ")
	print(japan_time_in_13_days(time_input))
	
	
if __name__ == "__main__":
	main()

