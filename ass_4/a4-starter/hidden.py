# Assigment 04, Task 04
# Name: Vikrom Narula
# Time spent: 48:00 hour

def is_hidden(s, t):
    """
    >>> is_hidden("welcometothehotelcalifornia","melon")
    True

    >>> is_hidden("welcometothehotelcalifornia","space")
    False

    >>> is_hidden("TQ89MnQU3IC7t6","MUIC")
    True

    >>> is_hidden("VhHTdipc07","htc")
    False

    >>> is_hidden("VhHTdipc07","hTc")
    True
    """

    y = 0
    for x in range(0, len(s) - 1):
        if t[y] == s[x] and y < len(t) - 1:
            y = y + 1
    if y == len(t) - 1:
        return True
    else:
        return False


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
