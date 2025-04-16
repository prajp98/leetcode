def findMode(self, root: Optional[TreeNode]) -> List[int]:
    def dfs(root):
        if not root:
            return
        count[root.val] += 1
        dfs(root.left)
        dfs(root.right)

    count = defaultdict(int)
    dfs(root)
    res = []
    m = max(count.values())
    for num, c in count.items():
        if count[num] == m:
            res.append(num)
    return res

def findMode(self, root: Optional[TreeNode]) -> List[int]:
    currNum,maxStreak,currStreak,res=0,0,0,[]
    def dfs(root):
        nonlocal currNum,maxStreak,currStreak,res
        if not root:
            return
        dfs(root.left)
        if root.val==currNum:
            currStreak+=1
        else:
            currNum=root.val
            currStreak=1
        if currStreak>maxStreak:
            maxStreak=currStreak
            res=[currNum]
        elif currStreak==maxStreak:
            res.append(currNum)
        dfs(root.right)
    dfs(root)
    return res