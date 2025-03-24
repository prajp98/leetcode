def wallsAndGates(self, rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    rows, cols = len(rooms), len(rooms[0])
    q = deque()
    l = 0
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                q.append((r, c))
    while q:
        l += 1
        for _ in range(len(q)):
            oldr, oldc = q.popleft()
            for dr, dc in directions:
                r, c = oldr + dr, oldc + dc
                if 0 <= r < rows and 0 <= c < cols and rooms[r][c] == 2147483647:
                    rooms[r][c] = l
                    q.append((r, c))