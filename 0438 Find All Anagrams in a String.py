def findAnagrams(self, s: str, p: str) -> List[int]:
    res = []
    pcount = Counter(p)
    scount = defaultdict(int)
    ns, np = len(s), len(p)
    for i in range(ns):
        scount[s[i]] += 1
        if i >= np:
            if scount[s[i - np]] == 1:
                del scount[s[i - np]]
            else:
                scount[s[i - np]] -= 1
        if scount == pcount:
            res.append(i - np + 1)
    return res
