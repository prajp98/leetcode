def findPermutation(self, s: str) -> list[int]:
    res = []
    stack = []
    for i in range(len(s) + 1):
        stack.append(i + 1)
        if i == len(s) or s[i] == 'I':
            while stack:
                res.append(stack.pop())
    return res