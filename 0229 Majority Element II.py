def majorityElement(self, nums: List[int]) -> List[int]:
    if not nums:
        return []
    num1, num2, cnt1, cnt2, res = None, None, 0, 0, []
    for num in nums:
        if num1 == num:
            cnt1 += 1
        elif num2 == num:
            cnt2 += 1
        elif cnt1 == 0:
            num1 = num
            cnt1 = 1
        elif cnt2 == 0:
            num2 = num
            cnt2 = 1
        else:
            cnt1 -= 1
            cnt2 -= 1
    for num in [num1, num2]:
        if nums.count(num) > len(nums) // 3:
            res.append(num)
    return res