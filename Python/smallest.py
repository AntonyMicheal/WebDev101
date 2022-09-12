a = int(input())
b = int(input())
c = int(input())
"""
if a < b:
    if a <c:
        print(f"{a} is the smallest")
    else:
        print(f"{c} is the smallest")
else:
    if b < c:
        print(f"{b} is the smallest")
    else:
        print(f"{c} is the smallest")
"""

if a<b and b<c:
    print(f"{a} is the smallest")
elif b<c and b<a:
    print(f"{b} is the smallest")
else:
    print(f"{c} is the smallest")