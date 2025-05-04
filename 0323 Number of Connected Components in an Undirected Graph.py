def countComponents(self, n: int, edges: List[List[int]]) -> int:
    adj = defaultdict(list)
    res = 0
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    visit = set()

    def dfs(node):
        if node in visit:
            return
        visit.add(node)
        for nei in adj[node]:
            dfs(nei)

    for i in range(n):
        if i not in visit:
            dfs(i)
            res += 1
    return res