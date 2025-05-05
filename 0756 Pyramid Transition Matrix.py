def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
    blocks = defaultdict(list)
    for a in allowed:
        blocks[a[:2]].append(a[2])

    @lru_cache(None)
    def dfs(row, nextRow, i):
        if len(row) == 1:
            return True
        if len(nextRow) + 1 == len(row):
            return dfs(nextRow, "", 0)
        for c in blocks[row[i:i + 2]]:
            if dfs(row, nextRow + c, i + 1):
                return True
        return False

    return dfs(bottom, "", 0)