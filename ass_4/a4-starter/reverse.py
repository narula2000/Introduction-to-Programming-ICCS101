# Assigment 04, Task 01
# Name: Vikrom Narula
# Time spent: 30:00 min
def rev_str(string):
    """Returns the reverse of the input string s, without using the built-in
    reverse mechanism.

    >>> rev_str("nowhere")
    'erehwon'

    >>> rev_str("gnimmargorpevoli")
    'iloveprogramming'

    >>> rev_str("y")
    'y'
    """
    buffer = ""
    for char in string:
        buffer = char + buffer
    return buffer


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
