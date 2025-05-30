import re


def is_filename_safe(filename: str) -> bool:
    """
    Check if the filename is valid.

    Rules:
    - Starts with a letter or number
    - Only contains letters, numbers, (), _, or -
    - Ends with .gif, .jpg, or .png

    Args:
        filename (str): Filename to check

    Returns:
        bool: True if valid, False if not
    """
		
    regex = r"^[A-Za-z0-9][A-Za-z0-9()_-]*\.(gif|jpg|png)$"
    return re.match(regex, filename) is not None


filename = "Some_Pic(2).png"

print(is_filename_safe(filename))
