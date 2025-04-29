def largestNumber(self, nums: List[int]) -> str:
    def compare(a, b):
        if a + b > b + a:
            return -1
        else:
            return 1

    for i in range(len(nums)):
        nums[i] = str(nums[i])
    nums.sort(key=cmp_to_key(compare))
    result = ''.join(nums)
    return "0" if result[0] == '0' else result