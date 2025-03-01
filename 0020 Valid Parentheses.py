def isValid(self, s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for ch in s:
        if ch in mapping:
            if not stack or mapping[ch] != stack.pop():
                return False
        else:
            stack.append(ch)
    return not stack