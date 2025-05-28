class Twitter:
    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(deque)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].appendleft((self.timestamp, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []

        users = self.following[userId].copy()
        users.add(userId)

        for uid in users:
            for time, tid in self.tweets[uid]:
                heapq.heappush(heap, (time, tid))
                if len(heap) > 10:
                    heapq.heappop(heap)
        return [tid for _, tid in sorted(heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)