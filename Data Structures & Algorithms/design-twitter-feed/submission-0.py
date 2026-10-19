class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.ppl = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time , tweetId))
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow(userId,userId)
        res = []
        for user in self.ppl[userId]:
            for timestamp, tweet in self.tweets[user]:
                res.append((timestamp,tweet))
        heapq.heapify(res)
        feeds = []
        while res and len(feeds) < 10:
            feeds.append(heapq.heappop(res)[1])
        return feeds

    def follow(self, followerId: int, followeeId: int) -> None:
        self.ppl[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.ppl[followerId].discard(followeeId)
        
