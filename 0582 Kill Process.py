def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
    tree = defaultdict(list)
    for c, p in zip(pid, ppid):
        tree[p].append(c)
    res = []

    def dfs(p):
        res.append(p)
        for c in tree[p]:
            dfs(c)

    dfs(kill)
    return res