def countBinarySubstrings(self, s: str) -> int:
    res, prev, cur = 0, 0, 1
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            res += min(prev, cur)
            prev = cur
            cur = 1
        else:
            cur += 1
    return res + min(prev, cur)