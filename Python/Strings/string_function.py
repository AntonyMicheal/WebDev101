str_1 = "   Hello World    "
str_2 = "abc123"
str_3 = "123"


print("\n strip() function usage \n")
print("original = "+str_1+"\n"+"after Strip:"+str_1.strip()+"the spaces are gone from the string")

print("\n Upper and Lower \n")
print("upper = "+str_1.upper()+", Lower = "+str_1.lower())

print("\n Capitalize() \n")
print("original = "+str_2+"\n"+"after capitalize: "+str_2.capitalize())

print("Ends with and starts with")

print((str_1.strip()).endswith("d"))
print((str_1.strip()).startswith("d"))

print(str_3.find("3"))
print(str_3.find("a"))

print(str_1.isalpha())
print(str_2.isalnum())
print(str_3.isdigit())
x = int(str_3)
print(type(x))

y = str_1.split()
print(y)

z = "_".join(y)
print(z)