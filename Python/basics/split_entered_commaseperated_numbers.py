"""
Write a Python program which accepts a sequence of comma-separated numbers from user and
generate a list and a tuple with those numbers.
"""

numbers = input("Enter some numbers: ")
list = numbers.split(",")
list_1 = []
for i in list:
    list_1.append(int(i))

print(list_1)
print(tuple(list_1))

