print("Hello World")

x = 10
print(type(x))

x = "antony"
print(type(x))

x = 10.55
print(type(x))

x = 10

print(id(x))

yi = x
print(id(yi))

x = "x"

print(id(x))

s = f"Hey How is {x}... he is a {yi}"
print(s)

print(type(True))

a, b = 10, 20
c = a > b
print(c)

a = "12"
print(a.isdigit())

x = range(5)
for i in x:
    print(i)
print("\n"*10)
for i in range(10):
    if i%2==0:
        continue
    print(i)