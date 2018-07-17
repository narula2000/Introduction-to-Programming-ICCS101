def zeroInsideFac(n):
    f_count=1
    count=0
    for i in range(1,n+1): #Fac n!
        f_count=f_count*i
    str_f=str(f_count)
    for j in range(1,len(str_f)): #Cut out zero from behind
        if str_f[-j]!='0':
            for k in str_f[:-j+1]:
                if k=='0': #Check Zero
                    count+=1
            return count
#for c,k in enumerate(str_f[:-j+1]): #Check for zero due to it's num(check zero before)
    #if k!='0':
        #for f in str_f[:-j+1][c:]:
            #if f=='0':
                    #count+=1
        #return count

assert(zeroInsideFac(5)==0)
assert(zeroInsideFac(16)==1)
assert(zeroInsideFac(37)==4)
print('Pass')


