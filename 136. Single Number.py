from collections import Counter


# 1. Brute Force     T:O(n²)     S:O(1)
def bruteForce(nums):
    n = len(nums)
    for i in range(n):
        c = 0
        for j in range(n):
            if nums[i] == nums[j]:
                c += 1
        if c == 1:
            return nums[i]


# 2. Hashmap     T:O(n)     S:O(n)
def hashmap(nums):
    freq = Counter(nums)
    for num, f in freq.items():
        if f == 1:
            return num


# 3. Math    T:O(n)     S:O(1)
def math(nums):
    return 2 * sum(set(nums)) - sum(nums)


# 4. XOR    T:O(n)     S:O(1)
# n^0 = n
# n^n = 0
def xor(nums):
    res = 0
    for n in nums:
        res = n ^ res
    return res


if __name__ == '__main__':
    arr = [0, 1, 0, 2, 1]
    print(bruteForce(arr))
    print(hashmap(arr))
    print(math(arr))
    print(xor(arr))
