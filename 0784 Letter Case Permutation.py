def letterCasePermutation(self, s: str) -> List[str]:
    res = []

    def dfs(i, cur):
        nonlocal res
        if i == len(s):
            res.append(cur)
            return
        if s[i].isalpha():
            dfs(i + 1, cur + s[i].lower())
            dfs(i + 1, cur + s[i].upper())
        else:
            dfs(i + 1, cur + s[i])

    dfs(0, "")
    return res

def letterCasePermutation(self, s: str) -> List[str]:
    res=[]
    def dfs(i,path):
        if i==len(s):
            res.append(''.join(path))
            return
        if s[i].isalpha():
            path.append(s[i].lower())
            dfs(i+1,path)
            path.pop()
            path.append(s[i].upper())
            dfs(i+1,path)
            path.pop()
        else:
            path.append(s[i])
            dfs(i+1,path)
            path.pop()
    dfs(0,[])
    return res
