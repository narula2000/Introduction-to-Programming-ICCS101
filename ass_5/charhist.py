# Assignment 05, Task 01
# Name: Vikrom Narula
# Time Spent: 1 hrs


def charHistogram(filename):
    text = open(filename, 'r')
    line = text.readlines()
    table = dict()
    for word in line:
        word = word.strip()
        for char in word:
            lowerChar = char.lower()
            if lowerChar in table:
                table[lowerChar] += 1
            else:
                table[lowerChar] = 1

    for key in table:
        print(key, (table[key] * '+'))
    text.close()
