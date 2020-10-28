# Assigment 04, Task 02
# Name: Vikrom Narula
# Time spent: 1:00 hour

def altSum(lst):
    """

    >>> altSum([])
    0
    >>> altSum([1,3,5,2])
    1
    >>> altSum([7,7,7,7])
    14
    >>> altSum([31,4,28,5,71])
    -59

    """
    if len(lst) == 0:
        return 0

    acc = lst[0]
    flip = 1
    for num in lst[1:]:
        acc += num * flip
        flip *= -1
    return acc


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
