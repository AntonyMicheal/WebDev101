list = [1, 5, 12, 2]

def concat_listdata(list):
    concatanated_string = ""
    for i in list:
        concatanated_string = concatanated_string + str(i)
    
    return concatanated_string

print(concat_listdata(list))