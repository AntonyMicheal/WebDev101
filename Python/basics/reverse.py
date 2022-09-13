number = int(input("Enter the number: "))

def reverse(n):
    reversed = 0
    while n > 0:
        rem = n%10
        reversed = reversed*10 + rem
        n//=10

    return reversed

print(reverse(number))