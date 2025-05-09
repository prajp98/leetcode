def isPerfectSquare(self, num: int) -> bool:
    if num < 2:
        return True
    l, r = 2, num // 2
    while l <= r:
        mid = (l + r) // 2
        square = mid * mid
        if square == num:
            return True
        elif square < num:
            l = mid + 1
        else:
            r = mid - 1
    return False