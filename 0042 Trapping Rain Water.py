# 1. Brute Force     T:O(n²)     S:O(1)
def bruteForce(height):
    res = 0
    n = len(height)
    for i in range(1, n - 1):
        maxLeft = height[i]
        for j in range(i):
            maxLeft = max(maxLeft, height[j])
        maxRight = height[i]
        for j in range(i + 1, n):
            maxRight = max(maxRight, height[j])
        res += (min(maxLeft, maxRight) - height[i])
    return res


# 2. Two pointer     T:O(n)     S:O(n)
def twoPointer(height):
    n = len(height)
    l = [0] * n
    r = [0] * n
    res = 0
    l[0] = height[0]
    r[n - 1] = height[n - 1]
    for i in range(1, n):
        l[i] = max(height[i], l[i - 1])
    for i in range(n - 2, -1, -1):
        r[i] = max(height[i], r[i + 1])

    for i in range(n):
        res += min(l[i], r[i]) - height[i]
    return res


# 2. Two pointer Space Optimised    T:O(n)     S:O(1)
def twoPointerOp(height):
    if not height:
        return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res


if __name__ == '__main__':
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(bruteForce(arr))
    print(twoPointer(arr))
    print(twoPointerOp(arr))
