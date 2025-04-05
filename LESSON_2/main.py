from random import randint as rnd

# names = [input("Enter a name: ").title() for i in range(int(input("How many names do you want? ")))]

nums = [rnd(1, 100) for i in range(3)]
nums = [str(n) for n in nums]
print(nums)



