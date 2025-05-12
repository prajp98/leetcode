def addBinary(self, a: str, b: str) -> str:
    p1 = len(a) - 1
    p2 = len(b) - 1
    carry = 0
    res = []

    while p1 >= 0 or p2 >= 0 or carry:
        total = carry

        if p1 >= 0:
            total += int(a[p1])
            p1 -= 1
        if p2 >= 0:
            total += int(b[p2])
            p2 -= 1

        res.append(str(total % 2))
        carry = total // 2

    return ''.join(reversed(res))