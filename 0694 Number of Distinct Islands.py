def numDistinctIslands(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    visited = set()
    shapes = set()

    def dfs(r, c, direction, path):
        if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] == 0:
            return
        visited.add((r, c))
        path.append(direction)
        dfs(r + 1, c, 'D', path)
        dfs(r - 1, c, 'U', path)
        dfs(r, c + 1, 'R', path)
        dfs(r, c - 1, 'L', path)
        path.append('B')

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not (r, c) in visited:
                path = []
                dfs(r, c, 'S', path)
                shapes.add(tuple(path))
    return len(shapes)