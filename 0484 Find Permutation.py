def findPermutation(self, s: str) -> list[int]:
    res = []
    stack = []
    for i in range(len(s) + 1):
        stack.append(i + 1)
        if i == len(s) or s[i] == 'I':
            while stack:
                res.append(stack.pop())
    return res

def findPermutation(self, s: str) -> list[int]:
    n = len(s)
    res = list(range(1, n + 2))  # Initial permutation [1 to n+1]

    i = 0
    while i < n:
        if s[i] == 'D':
            start = i
            while i < n and s[i] == 'D':
                i += 1
            res[start:i+1] = reversed(res[start:i+1])
        else:
            i += 1

    return res