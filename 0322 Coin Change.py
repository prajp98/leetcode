from collections import deque
from typing import List


def coinChange(self, coins: List[int], amount: int) -> int:
    def dfs(curSum):
        if curSum == amount:
            return 0
        if curSum > amount:
            return float('inf')
        minCoins = float('inf')
        for coin in coins:
            minCoins = min(1 + dfs(curSum + coin), minCoins)
        return minCoins

    res = dfs(0)
    return res if res != float('inf') else -1


def coinChange(self, coins: List[int], amount: int) -> int:
    memo={}
    def dfs(curSum):
        if curSum in memo:
            return memo[curSum]
        if curSum==amount:
            return 0
        if curSum>amount:
            return float('inf')
        minCoins=float('inf')
        for coin in coins:
            minCoins=min(1+dfs(curSum+coin),minCoins)
        memo[curSum]=minCoins
        return minCoins
    res=dfs(0)
    return res if res!=float('inf') else -1


def coinChange(self, coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0
    visit = set()
    visit.add(0)
    q = deque([0])
    res = 0
    while q:
        res += 1
        for i in range(len(q)):
            cur = q.popleft()
            for coin in coins:
                nxt = cur + coin
                if nxt == amount:
                    return res
                if nxt > amount or nxt in visit:
                    continue
                q.append(nxt)
                visit.add(nxt)
    return -1