def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []

    def dfs(root):
        nonlocal res
        if not root:
            return
        dfs(root.left)
        res.append(root.val)
        dfs(root.right)

    dfs(root)
    return res

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res