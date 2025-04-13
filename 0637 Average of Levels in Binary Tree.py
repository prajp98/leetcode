def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    if not root:
        return
    q = deque([root])
    res = []
    while q:
        n = len(q)
        s = 0
        for _ in range(n):
            node = q.popleft()
            s += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(s / n)
    return res