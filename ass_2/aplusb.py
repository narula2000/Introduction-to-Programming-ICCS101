# Assignment 02, Task 02
# Name: Vikrom Narula
# Collaborators: None
# TimeSpent: 3:00min

from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.
    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b<0:
        f = sub(a, b)
        return f
    else:
        f = add(a, b)
        return f
    return f(a,b)

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
