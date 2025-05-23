def isConvex(self, points: List[List[int]]) -> bool:
    def direction(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    d = 0
    n = len(points)
    for i in range(n):
        a = direction(points[i], points[(i + 1) % n], points[(i + 2) % n])
        if a:
            if not d:
                d = a
            elif a * d < 0:
                return False
    return True