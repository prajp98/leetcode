def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
    def dist(a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

    points = [p1, p2, p3, p4]
    s = set()
    for i in range(4):
        for j in range(i + 1, 4):
            d = dist(points[i], points[j])
            if d == 0:
                return False  # overlapping points
            s.add(d)
    return len(s) == 2  # one side length and one diagonal length