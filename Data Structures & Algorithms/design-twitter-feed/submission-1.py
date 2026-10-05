import heapq
class Twitter:
    # add yourself in the followers? 
    def __init__(self):
        self.follows=defaultdict(set)
        self.tweets=defaultdict(list)
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1 
        self.tweets[userId].append([-self.time,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        temp=self.follows[userId].copy()
        temp.add(userId)
        for following in temp: 
            tweets=self.tweets[following]
            for pair in tweets[-10:]:
                heapq.heappush(heap,pair)
        result=[]
        i=0 
        while heap and i<10: 
            result.append(heapq.heappop(heap)[1])
            i+=1
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)