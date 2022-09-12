a = int(input())
b = int(input())
c = int(input())

def sum_of_three(x,y,z):
    if x == y == z:
        return x*3*3
    else:
        return x+y+z

print(sum_of_three(a,b,c))