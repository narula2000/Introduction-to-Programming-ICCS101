def isAnagram(word1, word2, intab, outtab):
    indexw1=0
    indexin=0
    w1=[]
    finalw1=''
    switch= False
    for i in word1:
        w1.append(i)
    for i in range(len(w1)):
        for j in range(len(intab)):
            if w1[i]==intab[j]:
                indexw1= i
                indexin=j
                switch=True       
    if switch == True:            
        w1[indexw1]=outtab[indexin]
    for i in w1:
        finalw1+=i
        
    w2=[] 
    indexw2=0
    indexin2=0
    finalw2=''
    for i in word2:
        w2.append(i)
    for i in range(len(w2)):
        for j in range(len(intab)):
            if w2[i]==intab[j]:
                indexw2= i
                indexin2=j
                switch=True   
    if switch == True:            
        w2[indexw2]=outtab[indexin2]
        
    for i in w2:
        finalw2+=i
    if len(finalw1)==len(finalw2):
        for i in finalw1:
        
            if i not in finalw2:
                return False
            else:
                return True
    else:
        return False
