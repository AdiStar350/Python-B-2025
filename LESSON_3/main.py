"""
This script defines a function to find the first pair of consecutive elements in a list 
whose sum exceeds a predefined threshold. It demonstrates the function with two example datasets.
"""

# List of integers where some pairs of consecutive elements exceed the threshold
data_above_threshold = [10, 5, 12, 3, 9, 20, 1]

# List of integers where no pairs of consecutive elements exceed the threshold
data_below_threshold = [10, 5, 12, 3, 0, 9, 1]

# Threshold value to compare the sum of consecutive elements
THRESHOLD = 20

def find_pair_above_threshold(data):
    """
    Finds and prints the index of the first pair of consecutive elements in the list 
    whose sum exceeds the threshold. If no such pair exists, prints a message.
    
    Args:
        data (list): A list of integers to check.
    """
    # Iterate through the list, excluding the last element
    for index, value in enumerate(data[:-1]):
        # Check if the sum of the current element and the next element exceeds the threshold
        if value + data[index + 1] > THRESHOLD:
            # Print the index of the first pair that meets the condition
            print(f"Index: {index}")
            break  # Exit the loop once a pair is found
    else:
        # If no pair is found, print a message
        print("All pairs are below the threshold.")

# Call the function with the first dataset
find_pair_above_threshold(data_above_threshold)

# Call the function with the second dataset
find_pair_above_threshold(data_below_threshold)
