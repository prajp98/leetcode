def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

def isAnagram(self, s: str, t: str) -> bool:
    if len(s)!=len(t):
        return False
    sc=defaultdict(int)
    tc=defaultdict(int)
    for c in s:
        sc[c]+=1
    for c in t:
        tc[c]+=1
    for k in sc:
        if sc[k]!=tc[k]:
            return False
    return True

def isAnagram(self, s: str, t: str) -> bool:
    if len(s)!=len(t):
        return False
    count=defaultdict(int)
    for i in range(len(s)):
        count[s[i]]+=1
        count[t[i]]-=1
    for c in count.values():
        if c!=0:
            return False
    return True

