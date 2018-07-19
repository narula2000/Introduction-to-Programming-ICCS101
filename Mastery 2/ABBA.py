def generateAB(n):
    if n == 1:
        return ['A','B']
    else:
        a=generateAB(n-1)
        lst=[]
        for i in a:
           lst.append(i+'A')
           lst.append(i+'B')
        return lst
    
print(sorted(generateAB(3)))
