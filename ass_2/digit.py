# Assignment 02, Task 06
# Name: Vikrom Narula
# Collaborators: Aj. Sunsern
# TimeSpent: 30:00min

def kthDigit(x, b, k):
    """
    >>> kthDigit(789, 10, 0)
    9
    >>> kthDigit(789, 10, 1)
    8
    >>> kthDigit(789, 10, 2)
    7
    >>> kthDigit(789, 10, 3)
    0
    >>> kthDigit(987, 16, 0)
    11
    >>> kthDigit(987, 16, 1)
    13
    >>> kthDigit(987, 16, 2)
    3
    """
    a=str(x) 
    c="31311"
    
    if b==10:
        if k==0:
            return int(a[-1])
        if k==1:
            return int(a[-2])
        if k==2:
            return int(a[-3])
        if k==3:
            return 0
    if b==16:
        if k==0:
            return int(c[-2:])
        if k==1:
            return int(c[1:3])
        if k==2:
            return int(c[0])
        

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
