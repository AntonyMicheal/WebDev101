""" Write a Python program to count the occurrences of each word in a given sentence"""
"""
sentance = "the quick brown fox jumps over the lazy dog"
words = sentance.split(" ")
s = set(words)
for i in s:
    print(i,words.count(i))


"""

sentance = "the quick brown fox jumps over the lazy dog"
words = sentance.split(" ")

dictionary = {}
for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

print(dictionary)  
