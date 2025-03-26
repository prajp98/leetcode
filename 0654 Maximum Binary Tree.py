def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
    def findMax(arr, l, r):
        maxi = l
        for i in range(l, r + 1):
            if arr[i] > arr[maxi]:
                maxi = i
        return maxi

    def dfs(arr, l, r):
        if l > r:
            return
        maxi = findMax(arr, l, r)
        val = nums[maxi]
        root = TreeNode(val)
        root.left = dfs(arr, l, maxi - 1)
        root.right = dfs(arr, maxi + 1, r)
        return root

    return dfs(nums, 0, len(nums) - 1)