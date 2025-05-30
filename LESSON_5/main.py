# __Files__
# path = "/Users/adistrasser/Library/Mobile Documents/com~apple~CloudDocs/Studies/Python-B-2025/LESSON_5/temp.txt"
# path = "files/temp.txt"

# with open(path, mode='w') as file:
#     file.write("hello something\n")

# with open(path, mode='a') as file:
#     file.write("hello world")

# with open(path) as file:
#     cont = file.read()
#     print(cont)

# Q1
# rel_path = "files/new_file.txt"
# abs_path = "/Users/adistrasser/Library/Mobile Documents/com~apple~CloudDocs/Studies/Python-B-2025/LESSON_5/files/new_file.txt"

# with open(rel_path) as file:
#     cont = file.read()
#     print(cont)

# with open(abs_path) as file:
#     cont = file.read()
#     print(cont)


def colorize(text, color):
    if type(text) is not str:
        raise TypeError("text must be a str")
   
    colors = ("cyan", "yellow", "blue", "green", "red")

    if color not in colors:
        raise ValueError("color is incorrect")
    
    print(f"Printed {text} in {color}")

colorize("Hello", "red")
colorize("Hi", "chicken")
colorize(34, "red")
