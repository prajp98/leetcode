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

def reorganizeString(self, s: str) -> str:
    n = len(s)
    count = Counter(s)
    maxCh, maxFreq = max(count.items(), key=lambda x: x[1])
    if maxFreq>(n+1)//2:
        return ""
    res = [""] * n
    i = 0
    while count[maxCh] > 0:
        res[i] = maxCh
        i+=2
        count[maxCh] -= 1

    for ch,freq in count.items():
        while freq>0:
            if i>=n:
                i=1
            res[i]=ch
            i+=2
            freq-=1
    return ''.join(res)