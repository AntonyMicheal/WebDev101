list1 = [1,6,5,2,4]

def bubble_sort(list):
    for i in range(len(list)):
        swapped = False
        for j in range(1,len(list)-i):
            if list[j]<list[j-1]:
                temp = list[j]
                list[j] = list[j-1]
                list[j-1] = temp
                swapped = True
        if(not swapped):
            break

    return list
print(bubble_sort(list1))
