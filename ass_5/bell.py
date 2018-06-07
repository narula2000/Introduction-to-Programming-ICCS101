def loveTri(n):
    lst=[]
    e_lst=[]
    l_lst=[]
    
    for x in range(n):
        if x==0:
            lst.append(1)
            l_lst.append(lst)
        if x>0:
            e_lst=[lst[-1]]
            for y in range(len(lst)):
                e_lst.append(lst[y]+e_lst[y])
            lst=e_lst
            
            l_lst.append(e_lst)
    return l_lst
print(loveTri(5))








