
list_1 = [1,2,3,4,5,6,6,6,7,8,4,1,2,9,10]
x = set(list_1)
y = list(x)
print(y)
print(x)


"""-------------------           OR               --------------------------------"""


list_1 = [1,2,3,4,5,6,6,6,7,8,4,1,2,9,10]
list_2 = []

for i in list_1:
    if i not in list_2:
        list_2.append(i)

print(list_2)