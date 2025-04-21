def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    q = deque([root])
    res = []
    if not root:
        return res
    c = False
    while q:
        l = deque()
        for i in range(len(q)):
            node = q.popleft()
            if c:
                l.appendleft(node.val)
            else:
                l.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(list(l))
        c = not c
    return res

def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    q=deque([root])
    res=[]
    if not root:
        return res
    while q:
        l=[]
        for i in range(len(q)):
            node=q.popleft()
            l.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(l)
    for i in range(len(res)):
        if i%2==1:
            res[i]=res[i][::-1]
    return res