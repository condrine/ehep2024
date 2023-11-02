# script for solution to question 1 of exercise 2

# python imports
import math

# define lists
b = [2, 3, 4, 5, 6]  
p = [3, 4, 5, 6, 7]

# use loop to calculate power
print("\nUsing loop to calculate power")
print("==============================")
for base, power in zip(b, p):
    print(math.pow(base, power))

# use map to calculate power
print("\nUsing map to calculate power")
print("==============================")
val = list(map(math.pow, b, p))
print(val)

# use list comprehension
print("\nUsing list comprehension to calculate power")
print("============================================")
val = [math.pow(base, power) for base, power in zip(b, p)]
print(val)