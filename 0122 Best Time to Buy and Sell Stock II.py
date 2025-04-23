def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    d = 0
    for i in range(n - 1):
        if prices[i] < prices[i + 1]:
            d += (prices[i + 1] - prices[i])
    return d