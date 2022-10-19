string_list = ['Exercise', 'king', 'Queen', 'Hulk', 'Baby Shark']

longest_word = ""
for i in range(len(string_list)):
    if len(string_list[i]) > len(longest_word):
        longest_word = string_list[i]

print(longest_word, " ", len(longest_word))