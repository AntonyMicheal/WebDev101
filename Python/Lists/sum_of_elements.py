n = int(input("Enter the number of elements: "))
list=[]

def input_element(n, list):
    for i in range(n):
        element = int(input())
        list.append(element)
    
def sum_of(list):
    sum = 0
    for i in list:
        sum = sum+i
    return sum


input_element(n, list)
print(sum_of(list))