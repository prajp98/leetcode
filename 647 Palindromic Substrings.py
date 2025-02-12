#Brute Force T:O(n**3) S:O(n)
def countSubstrings(self, s: str) -> int:
    n = len(s)
    count = 0

    def isPali(sub):
        return sub == sub[::-1]

    for i in range(n):
        for j in range(i, n):
            if isPali(s[i:j + 1]):
                count += 1
    return count

#DP O(n**2) O(n**2)
def countSubstrings(self, s: str) -> int:
    n=len(s)
    count=0
    dp=[[False]*n for _ in range(n)]
    for i in range(n):
        dp[i][i]=True
        count+=1
    for i in range(n-1):
        if s[i]==s[i+1]:
            dp[i][i+1]=True
            count+=1
    for length in range(3,n+1):
        #Starting index of substring
        for i in range(n-length+1):
            #Ending index of substring
            j=i+length-1
            if s[i]==s[j] and (length==2 or dp[i+1][j-1]):
                dp[i][j]=True
                count+=1
    return count


#Expand around center O(n**2) O(1)
def countSubstrings(self, s: str) -> int:
    n=len(s)
    count=0
    def expand(l,r):
        nonlocal count
        while l>=0 and r<n and s[l]==s[r]:
            l-=1
            r+=1
            count+=1
    for i in range(n):
        expand(i,i)
        expand(i,i+1)
    return count