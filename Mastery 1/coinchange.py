def coinchange(v):
    lst=[]
    while (v-10)>=0:
        v=v-10
        lst.append(10)
    while (v-5)>=0:
        v=v-5
        lst.append(5)
    while (v-2)>=0:
        v=v-2
        lst.append(2)
    while (v-1)>=0:
        v=v-1
        lst.append(1)
    return lst

