
n = int(input("Enter the number of elements: "))
list=[]

def input_element(n, list):
    for i in range(n):
        element = int(input())
        list.append(element)

def multiply_all(list):
    multi = 1
    for i in list:
        multi = multi*i
    return multi


input_element(n, list)
print(multiply_all(list))