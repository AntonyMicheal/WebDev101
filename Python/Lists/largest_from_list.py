from insert_elements import input_element



def largest_element(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max


n = int(input("Enter the number of elements: "))
list=[]

input_element(n,list)
print("largest element is: ",largest_element(list))
