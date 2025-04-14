def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
    min1 = min2 = float('inf')

    def dfs(root):
        nonlocal min1, min2
        if not root:
            return
        if root.val < min1:
            min2, min1 = min1, root.val
        elif min2 > root.val > min1:
            min2 = root.val
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    return min2 if min2 < float('inf') else -1