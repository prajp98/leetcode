def wiggleSort(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    sorted_nums = sorted(nums)
    n = len(nums)
    mid = (n - 1) // 2
    end = n - 1
    for i in range(n):
        if i % 2 == 0:
            nums[i] = sorted_nums[mid]
            mid -= 1
        else:
            nums[i] = sorted_nums[end]
            end -= 1

def wiggleSort(self, nums):
    nums.sort()
    mid = (len(nums) + 1) // 2
    left, right = nums[:mid][::-1], nums[mid:][::-1]
    nums[::2], nums[1::2] = left, right