# Assigment 01 Task 05
# Name: Vikrom Narula
# Time spent: 1:00 hour


input = input("Enter your student ID:")


def decipher(input):
    cipher = 15485867**(22633) + 179424691**(7415)
    cipherString = str(cipher)
    idx = int(input[-3:])
    print(cipherString[-idx]+cipherString[idx-1])


decipher(input)
