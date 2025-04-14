def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
    min1 = root.val
    min2 = float('inf')

    def dfs(root):
        nonlocal min1, min2
        if not root:
            return
        if min2 > root.val > min1:
            min2 = root.val
        elif root.val == min1:
            dfs(root.left)
            dfs(root.right)

    dfs(root)
    return min2 if min2 < float('inf') else -1