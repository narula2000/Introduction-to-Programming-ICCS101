# Assignment 03, Task 06
# Name: Vikrom Narula
# Collaborators: None
# TimeSpent: 05:00min


def robust_avg(lst):
    """

    >>> round(robust_avg([3, 1, 2, 5, 9, 11, 4]), 4)
    4.6
    """

    lst.remove(max(lst))
    lst.remove(min(lst))
    return sum(lst) * 1.0 / (len(lst))


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
