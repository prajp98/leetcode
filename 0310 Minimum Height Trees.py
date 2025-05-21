def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    graph = defaultdict(list)
    degrees = [0] * n
    if n == 1:
        return [0]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
        degrees[a] += 1
        degrees[b] += 1
    leaves = deque([node for node in range(n) if degrees[node] == 1])
    while n > 2:
        num_leaves = len(leaves)
        n -= num_leaves
        for _ in range(num_leaves):
            leaf = leaves.popleft()
            for nei in graph[leaf]:
                degrees[nei] -= 1
                if degrees[nei] == 1:
                    leaves.append(nei)
    return list(leaves)