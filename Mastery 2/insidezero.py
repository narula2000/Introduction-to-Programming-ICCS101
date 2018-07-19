def Fac(n):
    if n==0:
        return 1
    else:
        a= Fac(n-1)* n
        return a

def zeroinsideFac(n):
    a= str(Fac(n))
    ans=[]
    for i in range(len(a)-1):
        if a[i]!='0':
            ans.append(i)
    if len(ans) <=3:
        return 0
    else:
        count= max(ans)
        final= a[:count+1]
    counter=0
    for i in final:
        if i == '0':
            counter+=1
    return counter
print(zeroinsideFac(37))      