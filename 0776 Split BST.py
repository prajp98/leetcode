def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
    def dfs(node):
        if not node:
            return [None, None]

        if node.val <= target:
            leftSubtree, rightSubtree = dfs(node.right)
            node.right = leftSubtree
            return [node, rightSubtree]
        else:
            leftSubtree, rightSubtree = dfs(node.left)
            node.left = rightSubtree
            return [leftSubtree, node]

    return dfs(root)