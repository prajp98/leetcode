def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    def dfs(root, curSum):
        if not root:
            return False
        curSum += root.val
        if not root.left and not root.right:
            return curSum == targetSum
        return dfs(root.left, curSum) or dfs(root.right, curSum)

    return dfs(root, 0)