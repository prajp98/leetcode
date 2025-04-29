def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    n = len(cost)
    res, curr = 0, 0
    if sum(gas) < sum(cost):
        return -1
    for i in range(n):
        curr += gas[i] - cost[i]
        if curr < 0:
            curr = 0
            res = i + 1
    return res