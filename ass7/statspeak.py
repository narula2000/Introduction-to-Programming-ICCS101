#Assignment 07, Task 03
#Name: Vikrom Narula
#Collaborations: 
#Time Spent: 30 min

class DataFrame:
    def __init__(self):
        self.data_items=[]
    def add(self, y):
        for i in y:
            if type(i)==int:
                self.data_items.append(i)
            else:
                for j in i:
                    self.data_items.append(j)
    def mean(self):
        return sum(self.data_items)/len(self.data_items)
    def mode(self):
        d=dict()
        for i in self.data_items:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=[j for j in d.keys() if d[j]==max(d.values())]
        return l[0]
    def percentile(self,r):
        l=sorted(self.data_items)
        return l[int((r/100)*len(self.data_items))]
    def stddev(self):
        t=0
        avg= self.mean()
        for i in self.data_items:
            t=t+((i-avg)**2)
        return t/len(self.data_items)

a=DataFrame()
a.add((5,34234,234242532,7,2132,(6)))
print(a.mean()==39046486.0)
print(a.mode()==5)
print(a.percentile(2)==5)
print(a.stddev()==7620299426765691.0)






