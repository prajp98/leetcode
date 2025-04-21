def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    c = defaultdict(int)
    res = []

    def dfs(root):
        if not root:
            return ""
        s = "(" + dfs(root.left) + ")" + str(root.val) + "(" + dfs(root.right) + ")"
        c[s] += 1
        if c[s] == 2:
            res.append(root)
        return s

    dfs(root)
    return res