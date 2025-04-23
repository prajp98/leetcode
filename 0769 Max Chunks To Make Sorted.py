def maxChunksToSorted(self, arr: List[int]) -> int:
    maxi = 0
    chunks = 0
    for i, num in enumerate(arr):
        maxi = max(maxi, num)
        if maxi == i:
            chunks += 1
    return chunks