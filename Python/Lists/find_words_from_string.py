""""Write a Python program to find the list of words that are longer than n from a given list of words."""

string1 = input("Enter the string: ")
n = int(input("Enter the number: "))


def string_finder(n,str):
    list_1 = str.split(" ")
    list_2 = []
    for i in list_1:
        if len(i)>n:
            list_2.append(i)
    return list_2

print(string_finder(n,string1))
        
