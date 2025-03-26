def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
    res = 0
    diff = float("-inf")

    def distance(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    for nut in nuts:
        res += (distance(nut, tree) * 2)
        diff = max(diff, distance(nut, tree) - distance(nut, squirrel))
    return res - diff