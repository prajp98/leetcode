def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    rows, cols = len(image), len(image[0])
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    visit = set()

    def dfs(r, c, first):
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != first or (r, c) in visit:
            return
        image[r][c] = color
        visit.add((r, c))
        for dr, dc in directions:
            dfs(r + dr, c + dc, first)

    dfs(sr, sc, image[sr][sc])
    return image
