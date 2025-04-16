def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
    res = []

    def dfs(root):
        if not root:
            return -1
        l = dfs(root.left)
        r = dfs(root.right)
        h = 1 + max(l, r)
        if len(res) == h:
            res.append([])
        res[h].append(root.val)
        return h

    dfs(root)
    return res