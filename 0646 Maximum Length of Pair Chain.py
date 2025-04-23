def findLongestChain(self, pairs: List[List[int]]) -> int:
    pairs.sort(key=lambda x: x[1])
    prevEnd = float('-inf')
    count = 0
    for pair in pairs:
        if pair[0] > prevEnd:
            count += 1
            prevEnd = pair[1]
    return count