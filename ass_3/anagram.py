def isAnagram(word1, word2):
    """

    >>> isAnagram("iceman","cinema")
    True
    """
    if len(word1) != len(word2):
        return False
    counter = 0
    for i in word1:
        for j in word2:
            if j == i:
                counter += 1
                break

    return counter == len(word1)


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
