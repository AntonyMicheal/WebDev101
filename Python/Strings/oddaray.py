
def oddarray(size, array):
    l = []
    for i in range(0,size):
        if array[i] % 2 != 0:
            l.append(i)

    return l

array = [1,2,3,4,5,6,7]
size = len(array)

x = oddarray(size, array)
print(x)