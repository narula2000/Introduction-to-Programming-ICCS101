class str2(str):
    def __repr__(self):
        return ''.join(('"', super().__repr__()[1:-1], '"'))




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
        while len(b)<((len(msg)//key)+1)*y:
            b=b+msg[x]
            x=x+key
            if x>=len(msg):
                x=0
            if x==0:
                x=x+y
            if len(b)==len(msg):
                return str2(b)
    


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
