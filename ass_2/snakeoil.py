# Assignment 02, Task 04
# Name: Vikrom Narula
# Collaborators: None
# TimeSpent: 3:00min
def price(vol):
    """
    >>> price(5)
    185.0
    >>> price(20)
    840.0
    >>> price(200)
    3298.0
    """

    if vol < 10:
        ship = 20 * vol
    elif vol >= 10 and vol <= 100:
        ship = 500
    elif vol > 100:
        ship = (vol * 17) * -0.03
    cost = vol * 17.0 + ship
    return cost


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
