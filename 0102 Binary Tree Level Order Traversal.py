def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    q = deque([root])
    res = []
    if not root:
        return []
    while q:
        l = []
        for i in range(len(q)):
            node = q.popleft()
            l.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(l)
    return res