# Assigment 04, Task 07
# Name: Vikrom Narula
# Time spent: 5:00 min

def primeMeatExtract(x):
    """

    >>> primeMeatExtract(1)
    True
    >>> primeMeatExtract(3)
    3
    >>> primeMeatExtract(4)
    True
    >>> primeMeatExtract(11)
    11
    >>> primeMeatExtract(642)
    3
    >>> primeMeatExtract(128)
    11
    >>> primeMeatExtract(886)
    True

    """

    def checkprime(number):
        if number <= 1:
            return False
        else:
            for i in range(2, number):
                if number % i == 0:
                    return False
            return True


    def plus_unit(number):
        acc = 0
        for unit in str(number):
            acc += int(unit)
        return acc


    while x > 9 and not checkprime(x):
        x = plus_unit(x)

    if checkprime(x):
        return x
    else:
        return True

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
