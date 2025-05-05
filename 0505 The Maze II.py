def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    rows, cols = len(maze), len(maze[0])
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[start[0]][start[1]] = 0
    q = deque([start])
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x, y
            steps = 0
            while 0 <= nx + dx < rows and 0 <= ny + dy < cols and maze[nx + dx][ny + dy] == 0:
                nx += dx
                ny += dy
                steps += 1
            if dist[x][y] + steps < dist[nx][ny]:
                dist[nx][ny] = dist[x][y] + steps
                q.append([nx, ny])
    res = dist[destination[0]][destination[1]]
    return res if res != float('inf') else -1