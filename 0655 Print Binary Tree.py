def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
    def getHeight(node):
        if not node:
            return 0
        return 1 + max(getHeight(node.left), getHeight(node.right))

    height = getHeight(root)
    width = (1 << height) - 1  # 2^height - 1
    res = [["" for _ in range(width)] for _ in range(height)]

    def fill(node, row, left, right):
        if not node:
            return
        mid = (left + right) // 2
        res[row][mid] = str(node.val)
        fill(node.left, row + 1, left, mid - 1)
        fill(node.right, row + 1, mid + 1, right)

    fill(root, 0, 0, width - 1)
    return res