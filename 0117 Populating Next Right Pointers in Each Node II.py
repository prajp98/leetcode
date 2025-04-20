def connect(self, root: 'Node') -> 'Node':
    if not root:
        return root
    q = deque([root])
    while q:
        n = len(q)
        prev = None
        for i in range(n):
            node = q.popleft()
            if prev:
                prev.next = node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            prev = node
    return root
