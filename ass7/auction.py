



class Bid:
    def __init__(self, bid_id, bidder_id, auction):
        self.bid_id,self.bidder_id,self.auction= bid_id,bidder_id,auction #bid_id is an integer other(str)
    def __str__(self):
        return 'The bid_id is {}. The bidder_id is {}. The auction is {}.'.format(self.bid_id,self.bidder_id,self.auction)
    def __repr__(self):
        return 'The bid_id is {}. The bidder_id is {}. The auction is {}.'.format(self.bid_id,self.bidder_id,self.auction)
    def __lt__(self,other):
        return self.bid_id<other.bid_id
    def __gt__(self, other):
        return self.bid_id>other.bid_id
    def __eq__(self,other):
        return self.bid_id==other.bid_id
    def __le__(self, other):
        return self.bid_id<=other.bid_id
    def __ge__(self, other):
        return self.bid_id>=other.bid_id

class Auction:
    def __init__(self, vary): #this can be auction, bidder_id (vary)
        self.vary=vary
    def placeBid(self,string):
        un= Bid()
    
    

