# Assigment 04, Task 06
# Name: Vikrom Narula
# Time spent: 1:30 hour

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
    finalTime = 0
    finalDistance = 0
    for log in activities:
        activity, time, distance = log.split(";")
        if activity == "jogging":
            timeSpent = time.split(":")[1]  # time
            hour, seconds = timeSpent.split(",")
            seconds = (int(hour) * 60) + int(seconds)
            distance = float(distance.split(":")[1]) * 1000
            finalDistance += distance
            finalTime += seconds
    speed = finalDistance / finalTime
    return speed


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
