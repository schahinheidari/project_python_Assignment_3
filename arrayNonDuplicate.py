#Assignment 3
import random

n = int(input("please give the length of your list"))
arr = []

while len(arr) < n:
	x = random.randint(0, 20)
    if x not in arr:
        arr.append(x)

print(arr)
    
	