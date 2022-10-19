""" Write a Python program to remove the characters which have odd index values of a given string"""

string = "abcdef"
str1 = ""
for i in range(len(string)):
    if i%2 == 0:
        str1 += string[i]

print(str1)