# Assigment 01 Task 05
# Name: Vikrom Narula
# Time spent: 30:00 min

input = input("Enter a 4-digit integer:")


def isTwisted(input):
    twisted = int(input[1:] + input[0])
    print("%d > %d ? %r" % (int(twisted), int(input), int(twisted) > int(input)))


isTwisted(input)
