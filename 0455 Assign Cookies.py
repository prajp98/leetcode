def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    gp = 0
    sp = 0
    while sp < len(s) and gp < len(g):
        # if satisfied,move both pointers
        if s[sp] >= g[gp]:
            gp += 1
        # else next bigger cookie
        sp += 1
    return gp