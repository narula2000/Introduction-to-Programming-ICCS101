#Assignment 05, Task 03 
#Name: Vikrom Narula

#Time Spent: 13 hrs


def stringmak(grid):
    h=''
    for li in grid:
        for w in li:
            h+=w
    return h


def wordSleuth(w, grid):
    lsring=stringmak(grid)
    l=[]
    gap=len(grid[0])
    cou=0
    for word in w:
        for longie in grid:
            if word in stringmak(longie):
                l.append(word)
        if word[0] in lsring:  #check vertical
            for b in range(len(lsring)):
                if word[0]==lsring[b]:
                    e=b
                    for letter in range(len(word)):
                        
                        if len(lsring)>=e+(gap*letter) and word[letter]==lsring[e+(gap*letter)]:
                            cou+=1
                        else:
                            cou=0
                    if cou==len(word):
                        l.append(word)
                        cou=0
        if word[0] in lsring:  #check righ down
                for b in range(len(lsring)):
                    if word[0]==lsring[b]:
                        e=b
                        for letter in range(len(word)):
                            
                            if len(lsring)>e+(gap*letter)+letter and word[letter]==lsring[e+(gap*letter)+letter] :
                                cou+=1
                            else:
                                cou=0
                        if cou==len(word):
                            l.append(word)
                            cou=0
                            
        if word[0] in lsring:  #check left up
                for b in range(len(lsring)):
                    if word[0]==lsring[b]:
                        e=b
                        for letter in range(len(word)):
                            
                            if len(lsring)>e+(gap*letter)+letter and word[letter]==lsring[e-(gap*letter)+letter] :
                                cou+=1
                            else:
                                cou=0
                        if cou==len(word):
                            l.append(word)
                            cou=0
    return list(set(l))





