s = set()
string = "restart"
string2 = ""
for i in string:
    if i not in s:
        s.add(i)
        string2+=i
    else:
        string2 += "$"

print(string2)
