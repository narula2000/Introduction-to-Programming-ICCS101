# Assignment 02, Task 03
# Name: Vikrom Narula
# Collaborators: None
# TimeSpent: 3:50min


def my_min(p, q, r):
    """Return the minimum of p,q, and r, without using min

    >>> my_min(3.0,1,9)
    1
    """
    if p < q and p < r:
        return p
    if q < p and q < r:
        return q
    else:
        return r


def my_mean(p, q, r):
    """Return the mean of p,q, and r

    >>> round(my_mean(3,7,4),5)
    4.66667
    """
    return (p+q+r)/3


def my_med(p, q, r):
    """Return the median of p,q, and r

    >>> my_med(13,5.0,12)
    12
    """

    # delete this comment line and add your code
    if (p > q and p < r) or (p < q and p > r):
        return p
    if (q > p and q < r) or (q < p and q > r):
        return q
    else:
        return r



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
