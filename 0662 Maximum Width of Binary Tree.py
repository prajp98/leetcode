def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    q = deque([(0, root)])
    res = 0
    while q:
        left, _ = q[0]
        right, _ = q[-1]
        res = max(res, right - left + 1)
        for _ in range(len(q)):
            i, node = q.popleft()
            if node.left:
                q.append((2 * i, node.left))
            if node.right:
                q.append((2 * i + 1, node.right))
    return res