from operator import countOf


def counter(list):
    count = 0
    for i in list:
        if i==4:
            count+=1
    return count


list = [1,2,4,4,4,6,4,6]
print(counter(list))

print(list.count(4))