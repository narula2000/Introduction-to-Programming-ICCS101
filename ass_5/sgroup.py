#Assignment 05, Task 05 
#Name: Vikrom Narula

#Time Spent: 24 hrs


def findmax(data):
    lst=[0]
    b=0
    
    for x in range(len(data)-1):
        a=data[x+1]-data[x]
        if a>b:
            b=a
            lst[0]=x
    return lst[0]
def maxxy(data):
    lst=[0]
    b=0
    
    for x in range(len(data)-1):
        a=data[x+1]-data[x]
        if a>b:
            b=a
            lst[0]=b
    return lst[0]
def checklstm(data):
    d=[]
    for y in data:
        if y not in d:
            d.append(y)
            d.append(findmax(y))
            d.append(maxxy(y))
    return d
def separate(data, k):
    l=[]
    g=data[:]
    el=[]
    el.append(g)
    vl=[3]
    b=0
    while k!=len(l):
        for ma in el:
            if maxxy(ma)>b:
                b=maxxy(ma)
                vl[0]=ma
                
        b=0
        ll=el
        for ch in ll:
            if ch==vl[0]:
                el.remove(vl[0])
                inx=findmax(vl[0])+1
                el.append(vl[0][:inx])
                el.append(vl[0][inx:])

        if len(el)==k:
            for u in el:
                l.append(u)
    return sorted(l)











