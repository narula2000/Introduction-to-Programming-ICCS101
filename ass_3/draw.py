# Assignment 03, Task 02
# Name: Vikrom Narula
# Collaborators: None
# TimeSpent: 80:00min


def triangle(k):
    """

    >>> triangle(1)
    *
    >>> triangle(3)
    ##*##
    #***#
    *****

    """
#    def star():
#        for a in range(1,k):
#            print("*"*a)
#
#    def pound():
#        for b in range(k-1,-1,-1):
#            print("#"*b)
#    return pound()+star()+pound()
#    for a in range(1,k):
#        x=("*"*a)
#    for b in range(k-1,-1,-1):
#        y=("#"*b)
#    print(y+x+y)
    for x in range(1, k+1):
        print("#"*(k-x)+"*"*(2*x-1)+"#"*(k-x))


def diamond(k):
    """

    >>> diamond(2)
    ##*##
    #***#
    #***#
    ##*##
    >>> diamond(4)
    ####*####
    ###***###
    ##*****##
    #*******#
    #*******#
    ##*****##
    ###***###
    ####*####

    """
    for x in range(1, k+1):
        print("#"*(k+1-x)+"*"*(2*x-1)+"#"*(k+1-x))
    for x in range(k, 0, -1):
        print("#"*(k+1-x)+"*"*(2*x-1)+"#"*(k+1-x))


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
