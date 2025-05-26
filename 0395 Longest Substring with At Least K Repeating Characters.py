def longestSubstring(self, s: str, k: int) -> int:
    def helper(sub: str) -> int:
        if len(sub) < k:
            return 0
        freq = Counter(sub)
        for i, ch in enumerate(sub):
            if freq[ch] < k:
                l = helper(sub[:i])
                r = helper(sub[i + 1:])
                return max(l, r)
        return len(sub)

    return helper(s)