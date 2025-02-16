#Brute Force T:O(2**n) S:O(n)
def numDecodings(self, s: str) -> int:
    def dfs(i):
        if i == len(s):
            return 1
        if s[i] == '0':
            return 0
        count = dfs(i + 1)
        if i + 1 < len(s) and int(s[i:i + 2]) <= 26:
            count += dfs(i + 2)
        return count

    return dfs(0)

#Memoization T:O(n) S:O(n)
def numDecodings(self, s: str) -> int:
    memo={}
    def dfs(i):
        if i==len(s):
            return 1
        if s[i]=='0':
            return 0
        if i in memo:
            return memo[i]
        count=dfs(i+1)
        if i+1<len(s) and int(s[i:i+2])<=26:
            count+=dfs(i+2)
        memo[i]=count
        return count
    return dfs(0)

#DP O(n) O(n)
def numDecodings(self, s: str) -> int:
    n=len(s)
    if not s or s[0] == '0':
        return 0
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        if s[i-1]!='0':
            dp[i]+=dp[i-1]
        if 10<=int(s[i-2:i])<=26:
            dp[i]+=dp[i-2]
    return dp[n]

#space DP O(n) O(1)
def numDecodings(self, s: str) -> int:
    n=len(s)
    if not s or s[0] == '0':
        return 0
    prev2=1
    prev1=1
    for i in range(2,n+1):
        temp=0
        if s[i-1]!='0':
            temp=prev1
        if 10<=int(s[i-2:i])<=26:
            temp+=prev2
        prev2=prev1
        prev1=temp
    return prev1