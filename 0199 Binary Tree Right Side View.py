def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    q = deque([root])
    if not root:
        return []
    res = []
    while q:
        res.append(q[-1].val)
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res