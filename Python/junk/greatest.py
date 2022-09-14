a = int(input())
b = int(input())
c = int(input())
max = 0
min = 0
if a>b:
    print(a)
    if a>c:
        max = a
        if c>b:
            min = b
        else:
            min = c
    else:
        max = c
        min = b
else:
    if b>c:
        max = b
        if a>c:
            min = c
        else:
            min = a
    else:
        max = c
        min = a

print(f"min = {min} max = {max}")


