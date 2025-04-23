def findLongestChain(self, pairs: List[List[int]]) -> int:
    pairs.sort(key=lambda x: x[1])
    currEnd = float('-inf')
    count = 0
    for pair in pairs:
        if pair[0] > currEnd:
            count += 1
            currEnd = pair[1]
    return count