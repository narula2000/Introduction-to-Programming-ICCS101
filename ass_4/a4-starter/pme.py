def checkprime(n):
    if n<2: return False
    else:
     divisible = False
     for d in range(2, n):
        if n % d == 0:
           divisible = True
           break
     # prime if none of these divide x
     return not divisible

def plus_unit(a):
    acc=0
    s=str(a)
    for b in range(1,len(s)+1):
        acc=acc+int(s[-b])
    return acc


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
    if x<=1:
        return True
    if x<=9 and x>1:
        if checkprime(x)== True:
            return x
        else:
            return True

    while checkprime(x)!=True and x>9:
        x=plus_unit(x)
    if x<=9 and x>1:
        if checkprime(x)== True:
            return x
        else:
            return True
    if checkprime(x)== True:
        return x



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
