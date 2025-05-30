def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    for letter in letters:
        if letter > target:
            return letter
    return letters[0]

def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    l=0
    r=len(letters)-1
    while l<=r:
        mid=(l+r)//2
        if letters[mid]<=target:
            l=mid+1
        else:
            r=mid-1
    if l==len(letters):
        return letters[0]
    else:
        return letters[l]