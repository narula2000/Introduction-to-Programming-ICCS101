def isprime(n):
    lst=[2]
    counter=0
    for x in range(3,n+1):
        for y in lst:
            if x%y!=0:
                
def sumdigit(n):
    m=str(n)
    k=0
    for x in range(1,len(m)+1):
        k=(int(m[-x])**2)+k
    return k

def happynum(n):
    lst=[]
    for y in range(1,n+1):
        x=y
        while x!=1 or x!=4:
            x=sumdigit(x)
            if x==1:
                lst.append(y)
                return lst
            if x==4:   
                return lst
        
def sumHP(n):
    lst=[]
    for x in isprime(n):
        if x in happynum(n):
            lst.append(x)
    return sum(lst)


sumHP(10)