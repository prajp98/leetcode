def findLonelyPixel(self, picture: List[List[str]]) -> int:
    rows, cols = len(picture), len(picture[0])
    row = [0] * rows
    col = [0] * cols
    res = 0
    for r in range(rows):
        for c in range(cols):
            if picture[r][c] == "B":
                row[r] += 1
                col[c] += 1
    for r in range(rows):
        for c in range(cols):
            if picture[r][c] == "B" and row[r] == 1 and col[c] == 1:
                res += 1
    return res