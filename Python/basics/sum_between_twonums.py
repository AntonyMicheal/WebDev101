a = int(input())
b = int(input())

def sum_of_two(a,b):
    sum = a+b
    if sum >= 15 and sum <= 20:
        return 20
    else:
        return sum

print(sum_of_two(a,b))
