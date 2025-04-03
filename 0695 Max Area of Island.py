def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    area = 0
    rows, cols = len(grid), len(grid[0])
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        x = 0
        for dr, dc in directions:
            x += dfs(r + dr, c + dc)
        return 1 + x

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                area = max(area, dfs(r, c))
    return area