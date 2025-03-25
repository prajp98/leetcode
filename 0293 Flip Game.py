def generatePossibleNextMoves(self, s: str) -> List[str]:
    res = []
    n = len(s)
    if n < 1:
        return res
    for i in range(n - 1):
        if s[i:i + 2] == "++":
            res.append(s[:i] + "--" + s[i + 2:])
    return res