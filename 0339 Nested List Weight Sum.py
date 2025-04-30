def depthSum(self, nestedList: List[NestedInteger]) -> int:
    def dfs(l, depth) -> int:
        total = 0
        for e in l:
            if e.isInteger():
                total += e.getInteger() * depth
            else:
                total += dfs(e.getList(), depth + 1)
        return total
    return dfs(nestedList, 1)