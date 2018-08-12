# Assigment 01 Task 05
# Name: VIkrom Narula
# Time spent: 30:00 min

x=input("Enter a 4-digit integer:")
def twist(x):
    return int(x)>int(x[1]+x[2]+x[3]+x[0]) != 1
print(str((int(x)))+" > "+str((int(x[1]+x[2]+x[3]+x[0])))+" ? "+str(twist(x)))