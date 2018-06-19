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

assert(findMe(9, [1,2,9,5,3,9])==2)
assert(findMe(7, [1,2,3,4,9])==None)
assert(findMe('nag',[1,2,3,'nag',4])==3)

print('Pass')