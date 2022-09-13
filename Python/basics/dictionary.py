d = {
    "usa":100,
    "india":300,
    "uk":200
    }

print(d.items())

print(len(d))

d["austraia"] = 400

print(d.items())
d.update({"antony":"micheal"})
print(d.items())

for i in d:
    print(i)