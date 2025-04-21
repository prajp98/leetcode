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

def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    def dfs(node):
        if not node or not node.left:
            return

        # Connect left -> right
        node.left.next = node.right

        # Connect right -> next.left (if next exists)
        if node.next:
            node.right.next = node.next.left

        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return root