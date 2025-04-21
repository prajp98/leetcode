def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    if not root:
        return []
    cols = defaultdict(list)
    q = deque([(root, 0)])
    mini, maxi = 0, 0
    while q:
        node, c = q.popleft()
        cols[c].append(node.val)
        mini = min(mini, c)
        maxi = max(maxi, c)
        if node.left:
            q.append((node.left, c - 1))
        if node.right:
            q.append((node.right, c + 1))
    for i in range(mini, maxi + 1):
        res.append(cols[i])
    return res