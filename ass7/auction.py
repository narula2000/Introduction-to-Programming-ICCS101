# Assignment 7 Task 4
# Name : Vikrom Narula
# collaboration : 1409
# Time spent: 68 hour


class Bid:
    def __init__(self, bid_id, bidder_id, auction):
        self.bid_id, self.bidder_id, self.auction = bid_id, bidder_id, auction

    def __str__(self):
        return 'bid _id {}bidder_id {} auction {}'.format(self.bid_id, self.bidder_id, self.auction)

    def __repr__(self):
        return 'bid _id: {}, bidder_id: {}, auction: {}'.format(self.bid_id, self.bidder_id, self.auction)

    def __lt__(self, other):
        return self.bid_id < other.bid_id

    def __gt__(self, other):
        return self.bid_id > other.bid_id

    def __le__(self, other):
        return self.bid_id <= other.bid_id

    def __ge__(self, other):
        return self.bid_id >= other.bid_id

    def __eq__(self, other):
        return self.bid_id == other.bid_id


class Auction:
    def __init__(self, auction):
        self.auction, self.name, self.bidd = auction, [], []

    def placeBid(self, bidder_id):
        if bidder_id not in self.name:
            self.name.append(bidder_id)
            self.bidd.append(Bid(len(self.bidd), bidder_id, self.auction))

    def price(self):
        price = 1
        price += len(self.name)*(1.5)
        return price

    def winner(self):
        l = []
        if self.bidder_id in self.name:
            l.append(self.bid_id)
            y = max(l)
        if y == self.bid_id:
            return (self.bid_id)
        else:
            return None


def CSV2List(csvFilename):
    l = []
    l2 = []
    l3 = []
    finallst = []
    instance = []
    newbid = []
    with open(csvFilename, 'r', newline='') as csvfile:
        r = csv.reader(csvfile)
        for i in r:
            l.append(i)
        count = 0
        for i in range(len(l[0])):
            if l[0][i] == 'bid_id':
                count = i
        for i in range(1, len(l)):
            l2.append(int(l[i][count]))
            l2.sort()
        for i in l2:
            for j in l:
                if str(i) in j:
                    l3.append(j)
        for i in range(len(l3)):
            bidid = l3[i][0]
            bidderid = l3[i][1]
            auction = l3[i][2]
            finallst.append(int(bidid))
            finallst.append(bidderid)
            finallst.append(auction)
        for i in range(len(finallst)+1):
            if len(instance) < 3:
                instance.append(finallst[i])
            else:
                newbid.append(tuple(instance))
                instance = []
                if len(finallst)/3 != len(newbid):
                    instance.append(finallst[i])
        return [Bid(i[0], i[1], i[2]) for i in newbid]


def mostPopularAuction(bidList):
    MP = {}
    for i in bidList:
        if i.auction in MP:
            MP[i.auction].placeBid(i.bidder_id)
        else:
            MP[i.auction] = Auction(i.auction)
            MP[i.auction].placeBid(i.bidder_id)
    finalsets = set()
    table = {a.auction: len(a.bidd) for a in MP.values()}
    print(table)
    most = max(table.values())
    for a in table.items():
        if a[1] == most:
            finalsets.add(a[0])
    return finalsets


def auctionWinners(bidList):
    MP = {}
    for i in bidList:
        if i.auction in MP:
            MP[i.auction].placeBid(i.bidder_id)
        else:
            MP[i.auction] = Auction(i.auction)
            MP[i.auction].placeBid(i.bidder_id)
    return MP
