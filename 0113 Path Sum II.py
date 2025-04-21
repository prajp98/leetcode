def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    res = []

    def dfs(root, currSum, path):
        if not root:
            return
        currSum += root.val
        path.append(root.val)
        if not root.left and not root.right:
            if currSum == targetSum:
                res.append(path[:])
        dfs(root.left, currSum, path)
        dfs(root.right, currSum, path)
        path.pop()

    dfs(root, 0, [])
    return res