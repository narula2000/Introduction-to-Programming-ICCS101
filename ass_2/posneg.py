# Assignment 02, Task 01
# Name: Vikrom Narula
# Collaborators: None
# TimeSpent: 5:00 min

def pos_neg(a, b, negative):
    """ pos_neg(a, b, negative) takes as input two integer values a and b,
    as well as a Boolean negative. The function returns True if one is
    negative and one is positive. Except if the parameter negative is True,
    then return True only if both are negative.

    >>> pos_neg(1, -1, False)
    True
    >>> pos_neg(-1, 1, False)
    True
    >>> pos_neg(-4, -5, True)
    True
    """

    if a > 0 and b < 0 and not negative:
        return True
    if a < 0 and b > 0 and not negative:
        return True
    if a < 0 and b < 0 and negative:
        return True
    else:
        return False

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
