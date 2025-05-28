def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    m = defaultdict(list)
    res = []
    for s in strs:
        m[tuple(sorted(s))].append(s)
    for v in m.values():
        res.append(v)
    return res