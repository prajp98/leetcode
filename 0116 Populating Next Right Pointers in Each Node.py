def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    if not root:
        return None
    q = deque([root])
    while q:
        prev = None
        for _ in range(len(q)):
            node = q.popleft()
            if prev:
                prev.next = node
            prev = node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return root