fruits = ["Apples", "Bananas", "dates", "Cherries"]
SEARCH_FRUIT = 'Bananas'
found = False

for index, value in enumerate (fruits) :
    if value == SEARCH_FRUIT:
        print(f"{SEARCH_FRUIT} found at index {index}")
        found = True
        break
else:
    print(f"{SEARCH_FRUIT} was not found in the list")
