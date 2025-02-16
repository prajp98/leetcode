# 1. Brute Force     T:O(n²)     S:O(1)
def bruteForce(height):
    n = len(height)
    maxArea = 0
    for i in range(n):
        for j in range(i + 1, n):
            maxArea = max(maxArea, min(height[i], height[j]) * (j - i))
    return maxArea


# 2. Two pointer     T:O(n)     S:O(1)
def twoPointer(height):
    l, r = 0, len(height) - 1
    res = 0

    while l < r:
        res = max(res, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res


if __name__ == '__main__':
    arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(bruteForce(arr))
    print(twoPointer(arr))
