def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
    m, n = len(picture), len(picture[0])
    rows, cols = defaultdict(int), defaultdict(int)
    total, dict = 0, defaultdict(int)
    grid = ["".join(i) for i in picture]

    for r in range(m):
        for c in range(n):
            if picture[r][c] == "B":
                rows[r] += 1
                cols[c] += 1
        dict[grid[r]] += 1

    for r in range(m):
        for c in range(n):
            if picture[r][c] == "B" and rows[r] == cols[c] == dict[grid[r]] == target:
                total += 1
    return total