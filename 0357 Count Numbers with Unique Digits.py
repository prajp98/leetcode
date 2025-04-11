def countNumbersWithUniqueDigits(self, n: int) -> int:
    count = 1
    def dfs(i, seen):
        nonlocal count
        if i == n:
            return
        for digit in range(10):
            if i == 0 and digit == 0:
                continue
            if digit not in seen:
                seen.add(digit)
                count += 1
                dfs(i + 1, seen)
                seen.remove(digit)

    dfs(0, set())
    return count

def countNumbersWithUniqueDigits(self, n: int) -> int:
    if n == 0:
        return 1
    res = 10
    unique = 9
    available = 9
    for i in range(2, n + 1):
        unique *= available
        res += unique
        available -= 1
    return res