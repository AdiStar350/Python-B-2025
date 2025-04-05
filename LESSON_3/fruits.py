# 1 + 2
my_big_banana_dict = {
    'Banana' : 99,
    'Apples' : 10,
    'Grapes' : 1
}

# 3
def display_my_nice_dict(my_dict):
    for k, v in my_dict.items():
        print(f"{k}  :  {v}")

    print()

display_my_nice_dict(my_big_banana_dict)

# 4
print(f"Banana : {my_big_banana_dict['Banana']}\n")

# 5
my_big_banana_dict['Apples'] -= 2
display_my_nice_dict(my_big_banana_dict)

# 6
print(f"{'Grapes' in my_big_banana_dict.keys() and my_big_banana_dict['Grapes'] > 0}\n")

# 7
display_my_nice_dict(my_big_banana_dict)


