#Assignment 3

n = int(input("please input your number: "))

if n % 2 == 0:
    for i in range(n):
        print("*#", end="")
else:
    for i in range(n):
        print("#*", end="")