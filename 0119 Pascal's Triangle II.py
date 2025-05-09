def getRow(self, rowIndex: int) -> List[int]:
    prev = [1]
    for i in range(rowIndex + 1):
        l = [1] * (i + 1)
        for j in range(1, i):
            l[j] = prev[j - 1] + prev[j]
        prev = l
    return l