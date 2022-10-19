"""Write a Python program to change a given string to
 a new string where the first and last chars have been exchanged"""

str = "Exchanging"

print(str[-1:] + str[1:-1] + str[0])
