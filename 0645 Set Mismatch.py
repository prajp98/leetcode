def findErrorNums(self, nums: List[int]) -> List[int]:
    count = defaultdict(int)
    res = [0, 0]
    for num in nums:
        count[num] += 1
    for i in range(1, len(nums) + 1):
        if count[i] == 2:
            res[0] = i
        if count[i] == 0:
            res[1] = i
    return res

def findErrorNums(self, nums: List[int]) -> List[int]:
    res=[]
    for num in nums:
        if (nums[abs(num)-1])<0:
            res.append(abs(num))
        else:
            nums[abs(num)-1]*=(-1)
    for i in range(len(nums)):
        if nums[i]>0:
            res.append(i+1)
            return res