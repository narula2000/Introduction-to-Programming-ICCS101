# Assignment 05, Task 01
# Name: Vikrom Narula
# Time Spent: 1 hrs


def charHistogram(filename):
    text = open(filename, 'r')
    line = text.readlines()
    table = dict()
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for words in line:
        word = words.strip()
        for char in word:
            lowerChar = char.lower()
            if lowerChar in table:
                table[lowerChar] += 1
            else:
                table[lowerChar] = 1
    for char in alphabets:
        for key in table.keys():
            if char == key:
                print(key, (table[key] * '+'))
    text.close()
