def removeComments(self, source: List[str]) -> List[str]:
    block = False
    res = []
    for line in source:
        i = 0
        if not block:
            newline = []
        while i < len(line):
            if line[i:i + 2] == '/*' and not block:
                block = True
                i += 1
            elif line[i:i + 2] == '*/' and block:
                block = False
                i += 1
            elif not block and line[i:i + 2] == '//':
                break
            elif not block:
                newline.append(line[i])
            i += 1
        if newline and not block:
            res.append("".join(newline))
    return res