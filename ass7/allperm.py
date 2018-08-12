#Assignment 07, Task 01
#Name: Vikrom Narula
#Collaborations: 
#Time Spent: 0.75 hrs


def all_perm(n):
    if n<1:
        return None
    if n==1:
        return {(1,)}
    else:
        b=all_perm(n-1)
        a=[]
        h=[]
        for m in b:
            for l in m:
                h.append(l)
            a.append(h)
            h=[]
        lst=[]
        for i in range(len(b)):
            for j in range(n):
                a[i].insert(j,n)
                lst.append(a[i])
                a=[]
                for m in b:
                    for l in m:
                        h.append(l)
                    a.append(h)
                    h=[]
                
        return set(tuple(mn) for mn in lst)