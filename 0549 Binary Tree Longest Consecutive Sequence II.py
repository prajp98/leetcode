def longestConsecutive(self, root: Optional[TreeNode]) -> int:
    longest = 0

    def dfs(node):
        nonlocal longest
        if not node:
            return 0, 0
        linc, ldec = dfs(node.left)
        rinc, rdec = dfs(node.right)
        inc = 1
        dec = 1
        if node.left:
            if node.val + 1 == node.left.val:
                inc = linc + 1
            elif node.val - 1 == node.left.val:
                dec = ldec + 1
        if node.right:
            if node.val + 1 == node.right.val:
                inc = max(inc, rinc + 1)
            elif node.val - 1 == node.right.val:
                dec = max(dec, rdec + 1)

        longest = max(longest, inc + dec - 1)
        return inc, dec

    dfs(root)
    return longest