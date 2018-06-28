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


