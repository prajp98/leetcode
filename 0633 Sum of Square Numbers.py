def judgeSquareSum(self, c: int) -> bool:
    l = 0
    r = int(math.sqrt(c))

    while l <= r:
        curr = l * l + r * r
        if curr == c:
            return True
        elif curr < c:
            l += 1
        else:
            r -= 1
    return False