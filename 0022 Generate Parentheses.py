def generateParenthesis(self, n: int) -> List[str]:
    res = []
    def dfs(s, countl, countr):
        if len(s) == n * 2:
            res.append("".join(s))
        if countl < n:
            s.append("(")
            dfs(s, countl + 1, countr)
            s.pop()
        if countr < countl:
            s.append(")")
            dfs(s, countl, countr + 1)
            s.pop()
    dfs([], 0, 0)
    return res