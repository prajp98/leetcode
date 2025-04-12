def partition(self, s: str) -> List[List[str]]:
    res = []

    def pali(s):
        return s == s[::-1]

    def dfs(start, path):
        if start == len(s):
            res.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if pali(sub):
                path.append(sub)
                dfs(end, path)
                path.pop()

    dfs(0, [])
    return res