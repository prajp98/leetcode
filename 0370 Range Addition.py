def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
    res = [0] * length
    for start, end, value in updates:
        res[start] += value
        end += 1
        if end < len(res):
            res[end] -= value
    for i in range(1, len(res)):
        res[i] += res[i - 1]
    return res