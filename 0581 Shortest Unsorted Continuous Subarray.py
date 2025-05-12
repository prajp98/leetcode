def findUnsortedSubarray(self, nums: List[int]) -> int:
    n = len(nums)
    r, maxi = -1, float('-inf')

    for i in range(n):
        maxi = max(maxi, nums[i])
        if nums[i] < maxi:
            r = i
    l, mini = n, float('inf')

    for i in range(n - 1, -1, -1):
        mini = min(mini, nums[i])
        if nums[i] > mini:
            l = i

    return max(0, r - l + 1)