def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
    l = 0
    maxi = 0
    h = {}
    for r in range(len(s)):
        h[s[r]] = r
        if len(h) > 2:
            del_index = min(h.values())
            del h[s[del_index]]
            l = del_index + 1
        maxi = max(maxi, r - l + 1)
    return maxi