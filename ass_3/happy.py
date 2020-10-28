
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
    acc = 0
    for unit in str(n):
        acc += (int(unit) ** 2)
    return acc


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
    while n != 1 and n != 4:
        n = sumOfDigitsSquared(n)
    return n == 1


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
    counter = 1
    happyNumber = 1
    while happyNumber - 1 != k:
        while isHappy(counter) is not True:
            counter += 1
        while isHappy(counter):
            happyNumber += 1
            counter += 1
        if happyNumber - 1 == k:
            return counter - 1


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
