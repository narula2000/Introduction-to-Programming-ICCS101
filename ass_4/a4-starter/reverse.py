def rev_str(s):
    """Returns the reverse of the input string s, without using the built-in
    reverse mechanism.

    >>> rev_str("nowhere")
    'erehwon'

    >>> rev_str("gnimmargorpevoli")
    'iloveprogramming'

    >>> rev_str("y")
    'y'
    """
    b=""
    for x in range(1,len(s)+1):
        if len(s)!=len(b):
            y=s[-x]
            b=b+y
        
        if len(s)==len(b):
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
