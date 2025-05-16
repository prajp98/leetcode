def decodeString(self, s: str) -> str:
    stack = []
    res = ""
    num = 0

    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '[':
            stack.append((res, num))
            res, num = "", 0
        elif ch == ']':
            prev, c = stack.pop()
            res = prev + res * c
        else:
            res += ch
    return res