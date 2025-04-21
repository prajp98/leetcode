def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    c = defaultdict(int)
    res = []

    def dfs(root):
        if not root:
            return ""
        s = "(" + dfs(root.left) + ")" + str(root.val) + "(" + dfs(root.right) + ")"
        c[s] += 1
        if c[s] == 2:
            res.append(root)
        return s

    dfs(root)
    return res

def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    subTreeMap = dict()
    count = defaultdict(int)
    res = []
    def dfs(node):
        if not node:
            return 0
        subTree = (dfs(node.left),node.val,dfs(node.right))
        if subTree not in subTreeMap:
            subTreeMap[subTree] = len(subTreeMap) + 1
        uid = subTreeMap[subTree]
        count[uid] += 1
        if count[uid] == 2:
            res.append(node)
        return uid
    dfs(root)
    return res