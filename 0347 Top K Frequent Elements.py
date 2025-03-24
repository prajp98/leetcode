def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    res, heap = [], []
    for num, c in count.items():
        heapq.heappush(heap, (-c, num))
    for i in range(k):
        res.append(heapq.heappop(heap)[1])
    return res

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count=Counter(nums)
    res=[]
    n=len(nums)
    freq=[[] for _ in range(n+1)]
    for num,c in count.items():
        freq[c].append(num)
    for i in range(len(freq)-1,-1,-1):
        for num in freq[i]:
            res.append(num)
            if len(res)==k:
                return res