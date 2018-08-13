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
    acc = 0
#    for x in range(0,len(lst)):
#        if x%2==0:
#            acc=acc+lst[x+1]
#        if x%2!=0:
#            acc=acc-lst[x+1]
#        if x==len(lst):
#            return acc
    if len(lst) == 0:
        return 0
    for x in range(0, len(lst)):

        if x == 0:
            acc = acc+lst[x]
        if x % 2 == 0 and x > 0:
            acc = acc-lst[x]
        if x % 2 != 0 and x > 0:
            acc = acc+lst[x]
        if len(lst) == x+1:
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
