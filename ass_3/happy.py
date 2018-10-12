
# Assignment 03, Task 05
# Name: Vikrom Narula
# Collaborators: None
# TimeSpent: 05:00min


def sumOfDigitsSquared(n):
    """

    >>> sumOfDigitsSquared(7)
    49
    >>> sumOfDigitsSquared(145)
    42
    >>> sumOfDigitsSquared(199)
    163
    """
    k = 0
    m = str(n)

    for x in range(0, len(m)):
        k = (int(m[-x])**2)+k
    return k


def isHappy(n):
    """

    >>> isHappy(100)
    True
    >>> isHappy(111)
    False
    >>> isHappy(1234)
    False
    >>> isHappy(989)
    True
    """
    r = n
    while r != 1 or r != 4:
        r = sumOfDigitsSquared(r)
        if r == 1 or r == 4:
            break

    if r == 4:
        return False
    if r == 1:
        return True


def kThHappy(k):
    """

    >>> kThHappy(2)
    7
    >>> kThHappy(3)
    10
    >>> kThHappy(11)
    49
    >>> kThHappy(19)
    97
    """
    c = 1
    h = 1
    while h-1 != k:
        while isHappy(c) != True:
            c = c+1
        while isHappy(c) == True:
            h = h+1
            c = c+1
        if h-1 == k:
            return c-1


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
