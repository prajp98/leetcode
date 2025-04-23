def longestPalindrome(self, s: str) -> int:
    count = Counter(s)
    length = 0
    odd_found = False

    for freq in count.values():
        if freq % 2 == 1:
            odd_found = True
            length += freq - 1
        else:
            length += freq
    return length + 1 if odd_found else length