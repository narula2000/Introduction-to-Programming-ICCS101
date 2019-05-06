class User:
    def __init__(self):
        self.follower = []

    def followedBy(self, that_user):
        if that_user not in self.follower and that_user != self:
            self.follower.append(that_user)

    def unfollowedBy(self, that_user):
        if that_user in self.follower:
            self.follower.remove(that_user)

    def isFollowedBy(self, that_user):
        if that_user in self.follower:
            return True
        else:
            return False
