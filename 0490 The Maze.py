def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    rows, cols = len(maze), len(maze[0])
    visit = set()
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    q = deque([start])
    visit.add((start[0], start[1]))
    while q:
        x, y = q.popleft()
        if [x, y] == destination:
            return True
        for dx, dy in directions:
            nx, ny = x, y
            while 0 <= nx + dx < rows and 0 <= ny + dy < cols and maze[nx + dx][ny + dy] == 0:
                nx += dx
                ny += dy
            if (nx, ny) not in visit:
                visit.add((nx, ny))
                q.append((nx, ny))
    return False