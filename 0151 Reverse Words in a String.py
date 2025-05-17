def reverseWords(self, s: str) -> str:
    res = s.strip().split()
    return ' '.join(res[::-1])