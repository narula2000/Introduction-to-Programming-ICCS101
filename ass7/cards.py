#Assignment 07, Task 02
#Name: Vikrom Narula
#Collaborations: 1409
#Time Spent: 8 hrs

def is_straight_flush(h): #Five cards in a sequence, all in the same suit.
    suit=dict()
    rank=['A','2','3','4','5','6','7','8','9','10','J','K','Q','A']
    lst_rank=[]
    count=0
    for i in h:
        if i[0] not in suit:
            suit[i[0]]=1
        else: suit[i[0]]+=1
        if i[1] not in lst_rank:
            lst_rank.append(i[1])
    if len(suit)==1:
        for c,k in enumerate(rank):
            for j in lst_rank:
                if j==k:
                    if sorted(lst_rank)==['10','A','J','K','Q']:
                        return True
                    else:
                        for v in rank[c:c+5]:
                            for l in lst_rank:
                                if v==l:
                                    count+=1
                        if count==5:
                            return True
                        else: return False
    else: return False

def is_four_a_kind(h): #All four cards of the same rank.
    count=0
    rank=dict()
    for i in h:
        if i[1] not in rank:
            rank[i[1]]=1
        else: rank[i[1]]+=1
    for j in rank:
        if rank[j]==4:
            count+=1
    if count==1:
        return True
    else: return False

def is_full_house(h): #Three of a kind with a pair.
    count=0
    rank=dict()
    for i in h:
        if i[1] not in rank:
            rank[i[1]]=1
        else: rank[i[1]]+=1
    if len(rank)==2:
        for j in rank:
            if rank[j]==3:
                count+=1
            elif rank[j]==2:
                count+=1
    else: return False
    if count==2:
        return True
    else: return False

def is_two_pair(h): #Two different pairs
    count=0
    rank=dict()
    for i in h:
        if i[1] not in rank:
            rank[i[1]]=1
        else: rank[i[1]]+=1
    for j in rank.keys():
        if rank[j]==2:
            count+=1
    if count==2:
        return True
    else: return False
#--------------------------------------------------------------------------------------
def deckMaker():
        lst=[]
        suite= ["Club","Diamond","Heart","Spade"]
        rank= ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        for i in suite:
            for j in rank:
                lst.append((i,j))
        return lst
def all_hand():
    deck=deckMaker()
    s_hand=[]
    for i1 in range(len(deck)):
        if i1<48:
            for i2 in range(i1+1,len(deck)):
                for i3 in range(i2+1,len(deck)):
                    for i4 in range(i3+1,len(deck)):
                        for i5 in range(i4+1,len(deck)):
                            s_hand.append((deck[i1],deck[i2],deck[i3],deck[i4],deck[i5]))
    return set(s_hand)

def all_straight_flush():
    return set([i for i in all_hand() if is_straight_flush(i)])

def all_four_of_a_kind():
    return set([i for i in all_hand() if is_four_a_kind(i)])

def all_full_house():
    return set([i for i in all_hand() if is_full_house(i)])

def all_two_pair():
    return set([i for i in all_hand() if is_two_pair(i)])
