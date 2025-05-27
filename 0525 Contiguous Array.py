def findMaxLength(self, nums: List[int]) -> int:
    count = 0
    maxi = 0
    mapi = {0: -1}
    for i, num in enumerate(nums):
        count += 1 if num == 1 else -1
        if count in mapi:
            maxi = max(maxi, i - mapi[count])
        else:
            mapi[count] = i
    return maxi