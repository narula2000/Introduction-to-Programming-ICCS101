def loveTri(n):
    lst=[]
    e_lst=[]
    l_lst=[]
    count=-1
    for x in range(n):
        if x==0:
            lst.append(1)
            l_lst.append(lst)
        if x>0:
            e_lst=[lst[-1]]
            for x in range(len(lst)):
                count+=1
                e_lst.append(lst[x]+e_lst[count])
                if x==(len(lst)-1):
                    count=-1
            lst=e_lst
            
            l_lst.append(e_lst)
    return l_lst
print(loveTri(5))








