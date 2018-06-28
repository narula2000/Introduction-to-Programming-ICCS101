# Assignment 06, Task 03
# Name:Vikrom Narula
# Time: 80 min 

def eto(lst):
    if len(lst)==1:
        return lst
    else:
        x=eto(lst[1:])
        if lst[0]%2==0:
            return [lst[0]]+x
        else:
            return x+[lst[0]]

assert(eto([1,2,3,4,5,6])==[2, 4, 6, 5, 3, 1])
assert(eto([1,2,36,9,2,43,17])==[2, 36, 2, 17, 43, 9, 1])
assert(eto([1,29,2,43,17])==[2, 17, 43, 29, 1])
assert(eto([1,2,3896,9,2,3,17])==[2, 3896, 2, 17, 3, 9, 1])
assert(eto([2,3,4,2,2,22,2,2,2])==[2, 4, 2, 2, 22, 2, 2, 2, 3])
