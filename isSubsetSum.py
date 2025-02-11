def subsetSum(arr, k):
    s = sum(arr)
    print(s)
    dp = [[False for _ in range(s + 1)] for _ in range(len(arr) + 1)]

    for i in range(len(arr) + 1):
        dp[i][0] = True

    for i in range(1, len(arr) + 1):
        for j in range(1, s + 1):

            if dp[i - 1][j]:
                dp[i][j] = True
            else:
                if dp[i - 1][j - arr[i - 1]] and arr[i - 1] <= s:
                    dp[i][j] = True
    for i in range(len(dp)):
        print(dp[i])
    return dp[len(arr)][k]


if __name__ == '__main__':
    res = [1, 2, 3]
    t = 5
    if subsetSum(res, t):
        print("Found a subset with given sum")
    else:
        print("No subset with given sum")
