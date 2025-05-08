def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    def dfs(l, r):
        if l > r:
            return
        m = (l + r) // 2
        root = TreeNode(nums[m])
        root.left = dfs(l, m - 1)
        root.right = dfs(m + 1, r)
        return root

    return dfs(0, len(nums) - 1)