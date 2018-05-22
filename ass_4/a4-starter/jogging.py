log_book = [
    "cycling;time:1,49;distance:2",
    "jogging;time:40,11;distance:6",
    "swimming;time:1,49;distance:1.2",
    "jogging;time:36,25;distance:5.3",
    "hiking;time:106,01;distance:8.29"
]

def jogging_average(activities):
    """

    >>> round(jogging_average(log_book), 4)
    2.4587
    """
    n_sec=0
    n_dis=0
    for x in activities:
        if "jogging;" in x:
            sec=int(x[13:15])*60+int(x[16:18])
            dis=float(x[28:])*1000
            n_sec=n_sec+sec
            n_dis=n_dis+dis
    return n_dis/n_sec
            
        
    

            
        



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
