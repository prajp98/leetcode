def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    res = []
    graph = defaultdict(dict)
    for i, (x, y) in enumerate(equations):
        graph[x][y] = values[i]
        graph[y][x] = 1.0 / values[i]

    def dfs(start, end, visit):
        if start in visit or start not in graph:
            return -1.0
        if start == end:
            return 1.0
        visit.add(start)
        for neighbor, value in graph[start].items():
            path_value = dfs(neighbor, end, visit)
            if path_value != -1.0:
                return value * path_value
        return -1.0

    for (x, y) in queries:
        res.append(dfs(x, y, set()))
    return res