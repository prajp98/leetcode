class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color={}
        for node in range(n):
            if node not in color:
                q=deque([node])
                color[node]="Red"
                while q:
                    current=q.popleft()
                    for nei in graph[current]:
                        if nei not in color:
                            color[nei]="Blue" if color[current] == "Red" else "Red"
                            q.append(nei)
                        elif color[nei] == color[current]:
                            return False
        return True