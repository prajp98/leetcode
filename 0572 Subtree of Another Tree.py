def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def sameTree(p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)
        return False

    def dfs(root):
        if not root:
            return False
        if not sameTree(root, subRoot):
            return dfs(root.left) or dfs(root.right)
        return True

    return dfs(root)


def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def serialize(node):
        if not node:
            return "N"
        return "#" + str(node.val) + " " + serialize(node.left) + " " + serialize(node.right)

    s = serialize(root)
    t = serialize(subRoot)
    return t in s