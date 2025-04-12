def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def dfs(i, path, total):
        if total == target:
            res.append(path[::])
            return
        if total > target or i >= len(candidates):
            return
        path.append(candidates[i])
        dfs(i + 1, path, total + candidates[i])
        path.pop()
        while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
            i += 1
        dfs(i + 1, path, total)

    candidates.sort()
    dfs(0, [], 0)
    return res

def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates.sort()
    def backtrack(start, path, total):
        if total == target:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if total + candidates[i] > target:
                break
            path.append(candidates[i])
            backtrack(i + 1, path, total + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return res