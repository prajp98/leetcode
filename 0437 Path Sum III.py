def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    def dfs(node, curr):
        nonlocal count
        if not node:
            return
        curr += node.val
        count += prefix[curr - targetSum]
        prefix[curr] += 1
        dfs(node.left, curr)
        dfs(node.right, curr)
        prefix[curr] -= 1

    count = 0
    prefix = defaultdict(int)
    prefix[0] = 1
    dfs(root, 0)
    return count