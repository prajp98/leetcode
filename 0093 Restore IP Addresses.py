def restoreIpAddresses(self, s: str) -> List[str]:
    res = []

    def dfs(start, path):
        if len(path) == 4:
            if start == len(s):
                res.append('.'.join(path))
            return
        for end in range(start + 1, min(start + 4, len(s) + 1)):
            sub = s[start:end]
            if (sub[0] == "0" and len(sub) > 1) or int(sub) > 255:
                continue
            path.append(sub)
            dfs(end, path)
            path.pop()

    dfs(0, [])
    return res