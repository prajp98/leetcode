def isStrobogrammatic(self, num: str) -> bool:
    m = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    l, r = 0, len(num) - 1
    while l <= r:
        if num[l] not in m or num[r] not in m:
            return False
        if m[num[l]] != num[r]:
            return False
        l += 1
        r -= 1
    return True