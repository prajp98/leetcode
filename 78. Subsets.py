# 1. Iterative    T:O(n*2ⁿ)  S:O(n*2ⁿ)
def iterative(nums):
    output = [[]]
    for num in nums:
        output += [curr + [num] for curr in output]
    return output


# 2. Backtracking     T:O(n*2ⁿ)     S:O(n)
def backtrack(nums):
    res = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)
        # decision NOT to include nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res


# 3. Shortened      T:O(n*2ⁿ)       S:O(n)
def shortened(nums):
    res = []

    def dfs(s, path):
        res.append(path)

        for i in range(s, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return res


if __name__ == '__main__':
    arr = [1, 2, 3]
    print(iterative(arr))
    print(backtrack(arr))
    print(shortened(arr))
