"""
Write a Python program to get a single string from two given strings, separated by a space 
and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz
"""

string1 = "abc"
string2 = "xyz"

string3 = string1.replace(string1[:2], string2[:2])
string4 = string2.replace(string2[:2], string1[:2])
print(string3, string4)