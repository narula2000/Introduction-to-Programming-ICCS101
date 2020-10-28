# Assigment 04, Task 04
# Name: Vikrom Narula
# Time spent: 48:00 hour

def is_hidden(string, hidden):
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

    iter = 0
    for i in range(len(string) - 1):
        if hidden[iter] == string[i] and iter < len(hidden) - 1:
            iter += 1
    if iter == len(hidden) - 1:
        iter = 0
    for i in range(len(string) - 1):
        if hidden[iter] == string[i] and iter < len(hidden) - 1:
            iter += 1

    return iter == len(hidden) - 1

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
