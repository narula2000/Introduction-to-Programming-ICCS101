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
    cun = 1
    n_lst = []
    if not lst:
        return []
    for x in range(0, len(lst)):
        if len(lst) != x + 1:
            if lst[x] == lst[x + 1]:
                cun = cun + 1

            if lst[x] != lst[x + 1]:
                n_lst.append(cun)
                n_lst.append(lst[x])
                cun = 1
        if len(lst) == x + 1:
            n_lst.append(cun)
            n_lst.append(lst[x])
            return n_lst


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
