# Assignment 02, Task 05
# Name: Vikrom Narula
# Collaborators: None
# TimeSpent: 6:00min


def nycHour(londonHour):
    """
    >>> nycHour(0)
    '7pm'
    >>> nycHour(11)
    '6am'
    >>> nycHour(23)
    '6pm'
    >>> nycHour(17)
    '12pm'
    >>> nycHour(5)
    '12am'
    """

    # delete this comment line, and write your code.
    if londonHour > 5 and londonHour < 17:
        return str(londonHour-5)+"am"
    if londonHour < 5:
        return str(londonHour+7)+"pm"
    if londonHour > 17:
        return str(londonHour-17)+"pm"
    if londonHour == 5:
        return "12am"
    else:
        return "12pm"


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
