#Assignment 05, Task 01 
#Name: Vikrom Narula

#Time Spent: 1 hrs

def charHistogram(filename):
    text= open(filename, 'r')
    line= text.readlines()
    table=dict()
    alp='abcdefghijklmnopqrstuvwxyz'
    for w in line:
        w_n= w.strip()
        for s in range(0,len(w_n)):
            for h in w[s]:
                l= h.lower()
                
                if l in table:
                    table[l]+=1
                else:
                    table[l]=1
#    for let in table.keys():
#        for al in range(0,len(alp)):
#            if let==alp[al]:
#                print(let, (table[let]*'+'))
    for al in range(0,len(alp)):
        for let in table.keys():
            if alp[al]==let:
                print(let, (table[let]*'+'))
    text.close()



