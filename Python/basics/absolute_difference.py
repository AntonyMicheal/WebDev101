
def difference(number):
    if number > 17:
        return abs(number-17)*2
    else:
        return abs(number-17)

n = int(input("Enter the number: "))
print(difference(n))