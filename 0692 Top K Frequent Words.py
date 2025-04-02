def topKFrequent(self, words: List[str], k: int) -> List[str]:
    heap = []
    res = []
    count = Counter(words)
    for word, c in count.items():
        heapq.heappush(heap, (-c, word))
    for i in range(k):
        _, word = heapq.heappop(heap)
        res.append(word)
    return res