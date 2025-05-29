def numWays(self, n: int, k: int) -> int:
    @lru_cache(None)
    def total_ways(i):
        if i == 1:
            return k
        if i == 2:
            return k * k
        return (k - 1) * (total_ways(i - 1) + total_ways(i - 2))

    return total_ways(n)

def numWays(self, n: int, k: int) -> int:
    if n == 1:
        return k
    if n == 2:
        return k * k
    dp = [0] * (n + 1)
    dp[1] = k
    dp[2] = k * k
    for i in range(3, n + 1):
        dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])
    return dp[n]

def numWays(self, n: int, k: int) -> int:
    if n == 1:
        return k
    two = k
    one = k * k
    for i in range(3, n + 1):
        t = (k - 1) * (one + two)
        two = one
        one = t
    return one