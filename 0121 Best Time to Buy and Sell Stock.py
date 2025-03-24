def maxProfit(self, prices: List[int]) -> int:
    mini = float('inf')
    d = 0
    for p in prices:
        d = max(d, p - mini)
        mini = min(mini, p)
    return d