def largestValues(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        maxi = float('-inf')
        for _ in range(len(q)):
            node = q.popleft()
            maxi = max(maxi, node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(maxi)
    return res