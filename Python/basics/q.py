#14610962141

li = [1,4,6,1,0,9,6,2,1,4,1,0]
s = []
print("hi")

for i in range(10):
    j = i
    list2 = []
    while li[i] == 1 and li[j+1] != 1:
        list2.append(li[j])
        j+=1
    s.append(list2)
print(s)





