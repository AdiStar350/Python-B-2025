numbers = [1, 3, 5, 7, 8, 9]

for num in numbers:
    if num % 2 == 0:
        print(num)
        break
else:
    print("Even not found")
