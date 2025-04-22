def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
    hashmap = {}
    l = 0
    res = 0
    for r in range(len(s)):
        hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
        while len(hashmap) > k:
            hashmap[s[l]] -= 1
            if hashmap[s[l]] == 0:
                del hashmap[s[l]]
            l += 1
        res = max(res, r - l + 1)
    return res