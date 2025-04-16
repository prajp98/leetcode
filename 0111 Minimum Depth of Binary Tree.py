def minDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    q = deque([root])
    l = 1
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if not node.left and not node.right:
                return l
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        l += 1