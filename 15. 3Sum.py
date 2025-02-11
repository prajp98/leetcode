# Given an integer array nums, return all the triplets
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# 1. Brute Force     T:O(n³)     S:O(1)
def bruteForce(nums):
    # Used a set to add only unique results.
    # Don't use it in the optimal solution.
    res = set()
    nums.sort()
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.add((nums[i], nums[j], nums[k]))
    return list(res)


# 2. Two pointer    T:O(n²)     S:O(1)
# Sort
# Unique nums[i]
# 2 pointer solution from 2Sum-II
def twoPointer(nums):
    res = []
    nums.sort()
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = n - 1
        while l < r:
            t = nums[i] + nums[l] + nums[r]
            if t > 0:
                r -= 1
            elif t < 0:
                l += 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res


if __name__ == '__main__':
    arr = [-6, -6, -3, -3, 0, 6, 5, 1, 12]
    print("List of triplets:")
    print("Brute force:")
    print(bruteForce(arr))
    print("Two pointer method:")
    print(twoPointer(arr))
