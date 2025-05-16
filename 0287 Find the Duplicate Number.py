def findDuplicate(self, nums: List[int]) -> int:
    for num in nums:
        index = abs(num)
        if nums[index] < 0:
            return index
        nums[index] *= -1

def findDuplicate(self, nums: List[int]) -> int:
    slow = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow