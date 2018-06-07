def findmaxdif(data):
    lst_m=[]
    dif_m=0
    for num in range(len(data)-1):
        dif=data[num+1]-data[num]
        if dif_m<dif:
            dif_m=dif
            lst_m.append(data[num],data[num+1],dif_m)
    return lst_m
def largegrp(data):
    lst=[]
    sl=findmaxdif(data)
    lst.append(data[sl[1]:])
    return lst
def smallgrp(data):
    lst=[]
    sl=findmaxdif(data)
    lst.append(data[:sl[0]])
    return lst
def separate(data, k):
    m_data=data[:]
    f_lst=[]
    lst_s1=smallgrp(data)
    lst_l1=largegrp(data)
    lst_l=lst_l1
    lst_s=lst_s1
    if k==2:
        f_lst.append(lst_s,lst_l)
    while len(f_lst)!=k:
        if findmaxdif(lst_s)[-1]> findmaxdif(lst_l)[-1]:
            f_lst.insert(0,smallgrp(lst_s))
            lst_s=smallgrp(lst_s)
            f_lst.insert(-1,largegrp(lst_s))
            lst_l=largegrp(lst_s)
        elif findmaxdif(lst_s)[-1]< findmaxdif(lst_l)[-1]:
            f_lst.insert(0,smallgrp(lst_l))
            lst_s=smallgrp(lst_l)
            f_lst.insert(-1,largegrp(lst_l))
            lst_l=largegrp(lst_l)
        else:
            f_lst.insert(0,smallgrp(lst_s))
            f_lst.insert()