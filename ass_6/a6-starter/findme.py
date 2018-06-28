# Assignment 06, Task 02
# Name:Vikrom Narula
# Time: 30 min 






def findMe(elt, lst):
    if elt not in lst:
        return None
    if lst[0]==elt:
        return 0
    else:
        n_lst=lst[1:]
        x=findMe(elt,n_lst)
        return x+1



