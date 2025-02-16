def maxProduct(self, nums: List[int]) -> int:
    res = float('-inf')
    n = len(nums)
    for i in range(n):
        s = 1
        for j in range(i, n):
            s *= nums[j]
            res = max(res, s)
    return res

def maxProduct(self, nums: List[int]) -> int:
    res=nums[0]
    mini,maxi= 1,1
    for num in nums:
        tmp=maxi*num
        maxi=max(num*maxi,num*mini,num)
        mini= min(tmp,num*mini,num)
        res=max(res,maxi)
    return res


