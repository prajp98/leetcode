def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))

def maxDepth(self, root: Optional[TreeNode]) -> int:
    q = deque()
    if root:
        q.append(root)
    l = 0
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        l += 1
    return l

def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            return 1+max(left,right)
        return dfs(root)