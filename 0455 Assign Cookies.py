def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    res = 0
    i = 0
    while i < len(s) and res < len(g):
        if s[i] >= g[res]:
            res += 1
        i += 1
    return res