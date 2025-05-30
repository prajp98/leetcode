def characterReplacement(self, s: str, k: int) -> int:
    count = defaultdict(int)
    maxi = 0
    l = 0
    res = 0
    for r in range(len(s)):
        count[s[r]] += 1
        maxi = max(maxi, count[s[r]])
        while (r - l + 1) - maxi > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res