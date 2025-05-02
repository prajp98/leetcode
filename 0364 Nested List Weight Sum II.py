def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
    def getMaxDepth(l, d):
        maxd = d
        for item in l:
            if not item.isInteger():
                maxd = max(maxd, getMaxDepth(item.getList(), d + 1))
        return maxd

    maxDepth = getMaxDepth(nestedList, 1)

    def dfs(l, d):
        total = 0
        for item in l:
            if item.isInteger():
                total += item.getInteger() * (maxDepth - d + 1)
            else:
                total += dfs(item.getList(), d + 1)
        return total

    return dfs(nestedList, 1)

def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
    q=deque(nestedList)
    res=0
    levelSum=0
    while q:
        for _ in range(len(q)):
            e = q.popleft()
            if e.isInteger():
                levelSum += e.getInteger()
            else:
                for sub in e.getList():
                    queue.append(sub)
        res+=levelSum
    return res