def reorganizeString(self, s: str) -> str:
    count = Counter(s)
    n = len(s)
    if max(count.values()) > (n + 1) // 2:
        return ''
    heap = []
    for char, freq in count.items():
        heapq.heappush(heap, (-freq, char))
    res = []
    prevFreq = 0
    prevChar = ''
    while heap:
        freq, char = heapq.heappop(heap)
        res.append(char)
        if prevFreq < 0:
            heapq.heappush(heap, (prevFreq, prevChar))
        prevFreq = freq + 1
        prevChar = char
    return ''.join(res)