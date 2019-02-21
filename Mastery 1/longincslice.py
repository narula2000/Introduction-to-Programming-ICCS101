
import time
import random

def randArray(size):
    return [random.randint(-1000, 1000) for _ in range(size)]

def longin(lst):
    counter=1
    c_lst=[]
    for x in range(0,len(lst)):
        if x<(len(lst)-1) and lst[x]<lst[x+1]:
            counter+=1
        else:
            c_lst.append(counter)
            counter=1
    print(max(c_lst))

tempList = randArray(200)
start = time.time()
longin(tempList)
#print(tempList)
print(time.time() - start)
