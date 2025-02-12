#Brute Force T:O(n**3) S:O(n)
def longestPalindrome(self, s: str) -> str:
    n = len(s)
    maxl = 0
    longest = ""

    def isPali(sub):
        return sub == sub[::-1]

    for i in range(n):
        for j in range(i, n):
            if isPali(s[i:j + 1]) and j - i + 1 > maxl:
                longest = s[i:j + 1]
                maxl = j - i + 1
    return longest

#DP O(n**2) O(n**2)
def longestPalindrome(self, s: str) -> str:
    n=len(s)
    #Stores starting and ending indexes
    res=[0,0]
    dp=[[False]*n for _ in range(n)]
    #Single characters are palindromes
    for i in range(n):
        dp[i][i]=True
    #Palindromes with length 2
    for i in range(n-1):
        if s[i]==s[i+1]:
            dp[i][i+1]=True
            res=[i,i+1]
    for length in range(3,n+1):
        #Starting index of substring
        for i in range(n-length+1):
            #Ending index of substring
            j=i+length-1
            if s[i]==s[j] and (length==2 or dp[i+1][j-1]):
                dp[i][j]=True
                res=[i,j]
    return s[res[0]:res[1]+1]

#Expand around center O(n**2) O(1)
def longestPalindrome(self, s: str) -> str:
    n=len(s)
    maxl=0
    longest=""
    def expand(l,r):
        while l>=0 and r<n and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]
    for i in range(n):
        l1=expand(i,i)
        if len(l1)>len(longest):
            longest=l1
        l2=expand(i,i+1)
        if len(l2)>len(longest):
            longest=l2
    return longest