from traceback import print_list


string = "google.com"

s = set(string)

for i in s:
    print(i, ": ", string.count(i))
