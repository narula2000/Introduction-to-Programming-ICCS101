# Assignment 05, Task 03
# Name: Vikrom Narula
# Time Spent: 13 hrs

def gridStringMaker(grid):
    buffer = ''
    for lst in grid:
        for char in lst:
            buffer += char
    return buffer


def stringMaker(lst):
    buffer = ''
    for char in lst:
        buffer += char
    return buffer


def checkVertical(word, string, char, size):
    counter = 0
    for letter in range(len(word)):
        if len(string) > char + (size * letter) and word[letter] == string[char + (size * letter)]:
            counter += 1
        else:
            break
    return counter


def checkRightDown(word, string, char, size):
    counter = 0
    for letter in range(len(word)):
        if len(string) > char + (size * letter) + letter and word[letter] == string[char + (size * letter) + letter]:
            counter += 1
        else:
            break
    return counter


def checkLeftDown(word, string, char, size):
    counter = 0
    for letter in range(len(word)):
        if len(string) > char + (size * letter) + letter and word[letter] == string[char - (size * letter) + letter]:
            counter += 1
        else:
            break
    return counter


def wordSleuth(grid, words):
    string = gridStringMaker(grid)
    lst = []
    size = len(grid[0])
    for word in words:
        for lst in grid:
            if word in stringMaker(lst):
                lst.append(word)

        if word[0] in string:
            for char in range(len(string)):
                if word[0] == string[char]:
                    if checkVertical(word, string, char, size) == len(word):
                        lst.append(word)
                    if checkRightDown(word, string, char, size) == len(word):
                        lst.append(word)
                    if checkLeftDown(word, string, char, size) == len(word):
                        lst.append(word)

    return list(set(lst))


assert(wordSleuth(
    [["r", "a", "w", "b", "i", "t"], ["x", "a", "y", "z", "c", "h"],
     ["p", "q", "b", "e", "i", "e"], ["t", "r", "s", "b", "o", "g"],
     ["u", "w", "x", "v", "i", "t"], ["n", "m", "r", "w", "o", "t"]],
    ["raw", "bit",   "rabbit", "bog", "the"]
))
