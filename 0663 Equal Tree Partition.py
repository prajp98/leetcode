def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
    sums = []

    def dfs(root):
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        total = root.val + left + right
        sums.append(total)
        return total

    total = dfs(root)
    sums.pop()
    return total // 2 in sums

