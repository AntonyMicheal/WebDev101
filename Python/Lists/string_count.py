
def input_element(n, list):
    for i in range(n):
        element = input()
        list.append(element)

def counter(list):
    count = 0
    for i in list:
        if len(i)>2 and i[0] == i[-1]:
            count+=1
    return count

n = int(input("Enter the number of elements: "))
list=[]
input_element(n,list)
print(counter(list))
