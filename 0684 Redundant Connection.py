def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    graph = defaultdict(list)

    def path(u, v):
        if u == v:
            return True
        visit.add(u)
        for nei in graph[u]:
            if nei not in visit:
                if path(nei, v):
                    return True
        return False

    for u, v in edges:
        visit = set()
        if u in graph and v in graph and path(u, v):
            return [u, v]
        graph[u].append(v)
        graph[v].append(u)
    return None

def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    def findLeader(v):
        if parent[v] != v:
            parent[v] = findLeader(parent[v])
        return parent[v]
    parent = list(range(len(edges) + 1))
    for a, b in edges:
        leadera = findLeader(a)
        leaderb = findLeader(b)
        if leadera == leaderb:
            return [a, b]
        parent[leadera] = leaderb
    return []