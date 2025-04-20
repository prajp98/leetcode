def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
    graph = defaultdict(list)
    target = None

    def dfs(root, parent):
        nonlocal target
        if not root:
            return
        if root.val == k:
            target = root
        if parent:
            graph[root].append(parent)
            graph[parent].append(root)
        dfs(root.left, root)
        dfs(root.right, root)

    dfs(root, None)
    q = deque([target])
    seen = set()
    while q:
        node = q.popleft()
        if not node.left and not node.right:
            return node.val
        seen.add(node)
        for nei in graph[node]:
            if nei not in seen:
                q.append(nei)