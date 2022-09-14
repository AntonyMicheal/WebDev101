from insert_elements import input_element

def smallest_element(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    
    return min


n = int(input("Enter the number of elements: "))
list=[]

input_element(n,list)
print("smallest element is: ",smallest_element(list))