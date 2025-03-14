def titleToNumber(self, columnTitle: str) -> int:
    res = 0
    i = 0
    for ch in reversed(columnTitle):
        res += (26 ** i) * (ord(ch) - ord('A') + 1)
        i += 1
    return res
