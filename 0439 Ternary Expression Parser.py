def parseTernary(self, expression: str) -> str:
    stack = []
    i = len(expression) - 1

    while i >= 0:
        ch = expression[i]
        if stack and stack[-1] == '?':
            stack.pop()
            t = stack.pop()
            stack.pop()
            f = stack.pop()
            stack.append(t if ch == 'T' else f)
        else:
            stack.append(ch)
        i -= 1
    return stack[-1]