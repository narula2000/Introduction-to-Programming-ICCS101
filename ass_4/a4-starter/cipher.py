def enc(msg, key):
    """

    >>> enc("abc",2)
    "acb"
    >>> enc("monosodium glutamate", 7)
    "mitouanmmo asgtoledu"
    >>> enc("polylogarithmicsubexponential", 3)
    "pygimseonaolatiuxntllorhcbpei"

    """
    x=0
    b=""
    for y in range(1,len(msg)):
        while len(b)<len(msg)*y:
            b=b+msg[x]
            x=x+key
            if x>=len(msg):
                x=y-1
            if x==0:
                x=x+y
        if len(b)==len(msg):
            return b
    


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
