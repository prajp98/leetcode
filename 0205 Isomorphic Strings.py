def isIsomorphic(self, s: str, t: str) -> bool:
    def compare(s, t):
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap and hashmap[s[i]] != t[i]:
                return False
            hashmap[s[i]] = t[i]
        return True

    return compare(s, t) and compare(t, s)