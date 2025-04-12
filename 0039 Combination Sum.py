def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def dfs(i, curr, total):
        if total == target:
            res.append(curr.copy())
            return
        if i >= len(candidates) or total > target:
            return
        # include
        curr.append(candidates[i])
        dfs(i, curr, total + candidates[i])
        # exclude
        curr.pop()
        dfs(i + 1, curr, total)

    dfs(0, [], 0)
    return res

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res=[]
    def dfs(start,total,l):
        if total==target:
            res.append(l[:])
            return
        if total>target:
            return
        for i in range(start,len(candidates)):
            l.append(candidates[i])
            dfs(i,total+candidates[i],l)
            l.pop()
    dfs(0,0,[])
    return res