# Assigment 04, Task 05
# Name: Vikrom Narula
# Time spent: 68:00 hour

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
    x = 0
    b = ""
    for y in range(1, len(msg)):
        while len(b) < ((len(msg) // key) + 1) * y:  # Says how many lines are in one set
            b = b + msg[x]  # Add by x index
            x = x + key  # Increases x by the key
            if x >= len(msg):
                x = 0
            if x == 0:
                x = x + y  # Next iteration
            if len(b) == len(msg):
                return str2(b)  # Spit out "..."


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
