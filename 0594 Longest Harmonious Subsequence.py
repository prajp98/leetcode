class Solution:
    def findLHS(self, nums):
        res = 0
        for i in range(len(nums)):
            count = 0
            flag = False
            for j in range(len(nums)):
                if nums[j] == nums[i]:
                    count += 1
                elif nums[j] + 1 == nums[i]:
                    count += 1
                    flag = True
            if flag:
                res = max(res, count)
        return res

class Solution:
    def findLHS(self, nums):
        nums.sort()
        res = 0
        prev_count = 0
        i = 0
        while i < len(nums):
            count = 1
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                count += 1
                i += 1
            if i > 0 and nums[i] - nums[i - count] == 1:
                res = max(res, count + prev_count)
            prev_count = count
            i += 1
        return res

class Solution:
    def findLHS(self, nums):
        count = Counter(nums)
        res = 0
        for key in count:
            if key + 1 in count:
                res = max(res, count[key] + count[key + 1])
        return res

class Solution:
    def findLHS(self, nums):
        from collections import defaultdict
        count = defaultdict(int)
        res = 0
        for num in nums:
            count[num] += 1
            if num + 1 in count:
                res = max(res, count[num] + count[num + 1])
            if num - 1 in count:
                res = max(res, count[num] + count[num - 1])
        return res