#Assignment 3

n = int(input("please input length of your array: "))
array = []

for i in range(n):
    x = int(input("please input your number: "))
    if (i == 0) or (x > array[- 1]):
        array.append(x)
    else:
        position = 0
        while (position < len(array)):
            if x <= array[position]:
                array.insert(position , x)
                break
            position = position + 1
print(array)