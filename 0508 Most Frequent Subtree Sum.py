def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
    count = defaultdict(int)
    res = []

    def dfs(root):
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        s = left + root.val + right
        count[s] += 1
        return s

    dfs(root)
    maxi = max(count.values())
    for s, c in count.items():
        if c == maxi:
            res.append(s)
    return res