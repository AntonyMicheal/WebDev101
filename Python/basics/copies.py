


#x = input()
#y = int(input())

def copy_maker(x,y):
    
    if len(x) >= y:
        sub = x[:y]
    else:
        sub = x[:len(x)]
    result = ""
    for i in range(y):
        result = result + sub

    return result

print(copy_maker('abcdef', 2))
print(copy_maker('p', 3))

