def getImportance(self, employees: List['Employee'], id: int) -> int:
    m = {}
    for e in employees:
        m[e.id] = e

    def dfs(id):
        e = m[id]
        total = e.importance
        for sub_id in e.subordinates:
            total += dfs(sub_id)
        return total

    return dfs(id)