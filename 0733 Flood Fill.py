def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    rows, cols = len(image), len(image[0])
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def dfs(r, c, src):
        if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] == color or image[r][c] != src:
            return
        image[r][c] = color
        for dr, dc in directions:
            dfs(r + dr, c + dc, src)

    dfs(sr, sc, image[sr][sc])
    return image
