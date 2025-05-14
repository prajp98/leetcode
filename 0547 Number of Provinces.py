def findCircleNum(self, isConnected: List[List[int]]) -> int:
    def dfs(city):
        for nei in range(len(isConnected)):
            if isConnected[city][nei] == 1 and nei not in visit:
                visit.add(nei)
                dfs(nei)

    visit = set()
    provinces = 0
    for i in range(len(isConnected)):
        if i not in visit:
            visit.add(i)
            dfs(i)
            provinces += 1
    return provinces