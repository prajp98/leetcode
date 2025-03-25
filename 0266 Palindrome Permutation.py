def canPermutePalindrome(self, s: str) -> bool:
    count = Counter(s)
    odds = 0
    for ch, c in count.items():
        if c % 2 != 0:
            odds += 1
    return odds <= 1

def canPermutePalindrome(self, s: str) -> bool:
    chars=set()
    for ch in s:
        if ch in chars:
            chars.remove(ch)
        else:
            chars.add(ch)
    return len(chars)<=1