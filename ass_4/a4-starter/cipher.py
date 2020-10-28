# Assigment 04, Task 05
# Name: Vikrom Narula
# Time spent: 68:00 hour

def enc(msg, key):
    """

    >>> enc("abc",2)
    'acb'
    >>> enc("monosodium glutamate", 7)
    'mitouanmmo asgtoledu'
    >>> enc("polylogarithmicsubexponential", 3)
    'pygimseonaolatiuxntllorhcbpei'

    """
    iter = 0
    buffer = ""
    for i in range(len(msg)):  # Next set of encoder
        while len(buffer) < ((len(msg) // key) + 1) * i:  # Says how many lines are in one set
            buffer += msg[iter]  # Add by x index
            iter += key  # Increases x by the key
            if iter >= len(msg):
                iter = 0
                iter += i  # Next iteration of index
            if len(buffer) == len(msg):
                return buffer  # Spit out "..."


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
