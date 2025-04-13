def findRelativeRanks(self, score: List[int]) -> List[str]:
    heap = []
    n = len(score)
    res = [0] * n
    for i, num in enumerate(score):
        heapq.heappush(heap, (-num, i))
    j = 1
    while heap:
        num, i = heapq.heappop(heap)
        if j == 1:
            res[i] = "Gold Medal"
        elif j == 2:
            res[i] = "Silver Medal"
        elif j == 3:
            res[i] = "Bronze Medal"
        else:
            res[i] = str(j)
        j += 1
    return res
def findRelativeRanks(self, score: List[int]) -> List[str]:
    maxScore = max(score)
    scoreToIndex = [-1] * (maxScore + 1)
    for i, s in enumerate(score):
        scoreToIndex[s] = i

    res = [0] * len(score)
    place = 1
    for s in range(maxScore, -1, -1):
        if scoreToIndex[s] >= 0:
            i = scoreToIndex[s]
            if place == 1:
                res[i] = "Gold Medal"
            elif place == 2:
                res[i] = "Silver Medal"
            elif place == 3:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(place)
            place += 1

    return res