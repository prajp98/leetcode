def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
    res = [0] * n
    stack = []
    prev = 0

    for log in logs:
        id, typ, time = log.split(":")
        id, time = int(id), int(time)
        if typ == "start":
            if stack:
                res[stack[-1]] += time - prev
            stack.append(id)
            prev = time
        else:
            res[stack.pop()] += time - prev + 1
            prev = time + 1
    return res