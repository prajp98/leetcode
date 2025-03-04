def nextGreaterElements(self, nums: List[int]) -> List[int]:
    stack = []
    n = len(nums)
    res = [-1] * n
    for _ in range(2):
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                res[index] = nums[i]
            stack.append(i)
    return res