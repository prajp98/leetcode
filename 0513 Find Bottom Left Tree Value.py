def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    q = deque([root])
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
    return node.val