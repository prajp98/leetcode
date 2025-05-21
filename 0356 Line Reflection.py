def isReflected(self, points: List[List[int]]) -> bool:
    xmin = float("inf")
    xmax = -float("inf")
    s = set()
    for x, y in points:
        xmax = max(xmax, x)
        xmin = min(xmin, x)
        s.add((x, y))
    center = (xmax + xmin) / 2
    for x, y in points:
        xref = center + (center - x)
        if (xref, y) not in s:
            return False
    return True