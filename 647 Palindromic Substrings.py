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