def findMode(self, root: Optional[TreeNode]) -> List[int]:
    def dfs(root):
        if not root:
            return
        count[root.val] += 1
        dfs(root.left)
        dfs(root.right)

    count = defaultdict(int)
    dfs(root)
    res = []
    m = max(count.values())
    for num, c in count.items():
        if count[num] == m:
            res.append(num)
    return res