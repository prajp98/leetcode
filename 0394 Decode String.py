def decodeString(self, s: str) -> str:
    stack = []
    for ch in s:
        if ch != "]":
            stack.append(ch)
        else:
            cur = ""
            while stack and stack[-1] != "[":
                cur = stack.pop() + cur
            stack.pop()
            num = ""
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            stack.append(cur * int(num))
    return "".join(stack)