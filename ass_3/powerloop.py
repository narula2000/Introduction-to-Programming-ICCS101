# Assignment 03, Task 01
# Name: Vikrom Narula
# Collaborators: None
# TimeSpent: 10:50min
def powerLoop(upTo):
    """

    >>> powerLoop(0)
    0 1
    >>> powerLoop(4)
    0 1
    1 11
    2 20
    3 18
    4 97
    """
    for x in range(upTo + 1):
        print(x, ((11 ** x) % 101))

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
