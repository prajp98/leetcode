def deserialize(self, s: str) -> NestedInteger:
    if s[0] != '[':
        return NestedInteger(int(s))
    stack = []
    num = 0
    neg = False
    for i, char in enumerate(s):
        if char == '-':
            neg = True
        elif char.isdigit():
            num = num * 10 + int(char)
        elif char == '[':
            stack.append(NestedInteger())
        elif char in ',]':
            if s[i - 1].isdigit():
                if neg:
                    num = -num
                stack[-1].add(NestedInteger(num))
            num = 0
            neg = False
            if char == ']' and len(stack) > 1:
                nested = stack.pop()
                stack[-1].add(nested)
    return stack.pop()
