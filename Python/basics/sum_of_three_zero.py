"""Write a Python program to sum of three given integers. However, if two values are equal sum will be zero"""

a = int(input())
b = int(input())
c = int(input())

def sum_of_three(a,b,c):
    if a == b or b==c or a ==c:
        return 0
    else:
        return a+b+c

print(sum_of_three(a,b,c))








