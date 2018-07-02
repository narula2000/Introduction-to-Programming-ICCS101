#Assignment 07, Task 03
#Name: Vikrom Narula
#Collaborations: 
#Time Spent: 30 min

class DataFrame:
    def __init__(self):
        self.data_items=[]
    def add(self, y):
        if type(y)==int:
            return self.data_items.append(y)
        else:
            for i in y:
                return self.data_items.append(i)
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
        avg= mean()
        for i in self.data_items:
            t=t+((i-avg)**2)
        return t/len(self.data_items)







