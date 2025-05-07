def numberOfBoomerangs(self, points: List[List[int]]) -> int:
    n = 0
    for a1, b1 in points:
        count = {}
        for a2, b2 in points:
            key = (a2 - a1) ** 2 + (b2 - b1) ** 2
            if key in count:
                n += 2 * count[key]
                count[key] += 1
            else:
                count[key] = 1
    return n