def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    res = float('inf')
    l = []

    def dfs(root):
        if not root:
            return
        dfs(root.left)
        l.append(root.val)
        dfs(root.right)

    dfs(root)
    for i in range(len(l) - 1):
        res = min(res, l[i + 1] - l[i])
    return res

def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    res=float('inf')
    prev=None
    def dfs(root):
        nonlocal res,prev
        if not root:
            return
        dfs(root.left)
        if prev is not None:
            res=min(res,root.val-prev)
        prev=root.val
        dfs(root.right)
    dfs(root)
    return res