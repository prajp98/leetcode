def simplifyPath(self, path: str) -> str:
    stack = []
    for part in path.split("/"):
        if part == "..":
            if stack:
                stack.pop()
        elif part == "." or not part:
            continue
        else:
            stack.append(part)
    return "/" + "/".join(stack)
