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

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    curr = root
    while curr:
        if not curr.left:
            res.append(curr.val)
            curr = curr.right
        else:
            pre = curr.left
            while pre.right and pre.right != curr:
                pre = pre.right

            if not pre.right:
                pre.right = curr  # Make thread
                curr = curr.left
            else:
                pre.right = None  # Remove thread
                res.append(curr.val)
                curr = curr.right
    return res