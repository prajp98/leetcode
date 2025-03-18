def convertToTitle(self, columnNumber: int) -> str:
    res = []
    while columnNumber > 0:
        columnNumber -= 1
        res.append(chr(columnNumber % 26 + ord('A')))
        columnNumber //= 26
    res = ''.join(res)
    return res[::-1]