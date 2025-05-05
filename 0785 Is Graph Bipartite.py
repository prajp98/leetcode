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

def isBipartite(self, graph: List[List[int]]) -> bool:
    color = {}

    def dfs(node, c):
        if node in color:
            return color[node] == c
        color[node] = c
        next_color = "Blue" if c == "Red" else "Red"
        for neighbor in graph[node]:
            if not dfs(neighbor, next_color):
                return False
        return True

    for i in range(len(graph)):
        if i not in color:
            if not dfs(i, "Red"):
                return False
    return True