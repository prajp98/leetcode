def guessNumber(self, n: int) -> int:
    l = 1
    r = n
    while l <= r:
        mid = (l + r) // 2
        res = guess(mid)
        if res == 0:
            return mid
        elif res < 0:
            r = mid - 1
        else:
            l = mid + 1
    return -1