# Assignment 05, Task 05
# Name: Vikrom Narula
# Time Spent: 24 hrs


def findMaxGapOfList(data):
    max = 0
    idx = 0
    for i in range(len(data) - 1):
        gap = data[i + 1] - data[i]
        if gap > max:
            max = gap
            idx = i
    return (idx, max)


def findMaxGapList(data):
    max = 0
    maxGapLst = []
    for lst in data:
        if findMaxGapOfList(lst)[1] > max:
            max = findMaxGapOfList(lst)[1]
            maxGapLst = lst
    return maxGapLst


def separate(data, k):
    data = [data[:]]
    while k != len(data):
        maxGapList = findMaxGapList(data)
        data.remove(maxGapList)
        split = findMaxGapOfList(maxGapList)[0] + 1
        data.append(maxGapList[:split])
        data.append(maxGapList[split:])

    return sorted(data)
