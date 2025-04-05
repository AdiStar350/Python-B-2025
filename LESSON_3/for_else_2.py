str_list = ["apple", "banana", "cherry!", "date", "elderberry", "fig", "grape"]

for s in str_list:
    if not s.isalpha():
        print(f"{s} is not all alphabetic characters")
        break
else:
    print("list is valid")
