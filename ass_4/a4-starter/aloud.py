# Assigment 04, Task 03
# Name: Vikrom Narula
# Time spent: 1:00 hour


def readAloud(lst):
    """
    >>> readAloud([])
    []
    >>> readAloud([1,1,1])
    [3, 1]
    >>> readAloud([-1,2,7])
    [1, -1, 1, 2, 1, 7]
    >>> readAloud([3,3,8,-10,-10,-10])
    [2, 3, 1, 8, 3, -10]
    >>> readAloud([3,3,1,1,3,1,1])
    [2, 3, 2, 1, 1, 3, 2, 1]
    """
    counter = 1
    answer = []
    if not lst:
        return []
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            counter += 1
        else:
            answer.append(counter)
            answer.append(lst[i])
            counter = 1
    answer.append(counter)
    answer.append(lst[-1])
    return answer


###########################################################################
# Please don't mind me living down here. I provide some initial testing for
# your code. Run me (e.g., using the run button in Spyder).
###########################################################################
# Simple Tests
###########################################################################
if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
###########################################################################
