def partition(self, s: str) -> List[List[str]]:
    res = []
    part = []
    def isPali(sub):
        return sub==sub[::-1]
    def dfs(i):
        if i>=len(s):
            res.append(part[::])
            return
        for j in range(i,len(s)):
            sub=s[i:j+1]
            if isPali(sub):
                part.append(sub)
                dfs(j+1)
                part.pop()
    dfs(0)
    return res