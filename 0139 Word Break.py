# Solution 1: Recursive Brute Force
# Time Complexity: O(2^n) where n is the length of string s
# Space Complexity: O(n) for the recursion stack depth
from collections import deque


def wordBreak_bruteforce(s: str, wordDict: list[str]) -> bool:
    def dfs(start):
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordDict and dfs(end):
                return True
        return False

    return dfs(0)


# Solution 2: Memoization (Top-down DP)
# Time Complexity: O(n * m * k) where:
# - n is the length of string s
# - m is the number of words in wordDict
# - k is the average length of words in wordDict
# Space Complexity: O(n) for memoization dictionary and recursion stack
def wordBreak_memoization(s: str, wordDict: list[str]) -> bool:
    wordSet = set(wordDict)
    memo = {}

    def dfs(start):
        if start in memo:
            return memo[start]
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordSet and dfs(end):
                memo[start] = True
                return True
        memo[start] = False
        return False

    return dfs(0)


# Solution 3: Tabulation (Bottom-up DP)
# Time Complexity: O(n * m * k) where:
# - n is the length of string s
# - m is the number of words in wordDict
# - k is the average length of words in wordDict
# Space Complexity: O(n) for the dp array
def wordBreak_tabulation(s: str, wordDict: list[str]) -> bool:
    wordSet = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    return dp[-1]


# Solution 4: Optimized with Set and Word Length Optimization
# Time Complexity: O(n * k) where:
# - n is the length of string s
# - k is the maximum word length in wordDict
# Space Complexity: O(n + m) where:
# - O(n) for the dp array
# - O(m) for the word_set where m is total characters in wordDict
def wordBreak_optimized(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict)
    n = len(s)
    max_word_length = max(len(word) for word in wordDict)
    min_word_length = min(len(word) for word in wordDict)

    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(min_word_length, n + 1):
        for length in range(min_word_length, min(i + 1, max_word_length + 1)):
            if dp[i - length] and s[i - length:i] in word_set:
                dp[i] = True
                break

    return dp[n]

#BFS
def wordBreak(self, s: str, wordDict: list[str]) -> bool:
    wordSet=set(wordDict)
    n=len(s)
    q=deque([0])
    visit=set([0])
    while q:
        start=q.popleft()
        if start==n:
            return True
        for end in range(start+1,n+1):
            if end not in visit and s[start:end] in wordSet:
                q.append(end)
                visit.add(end)
    return False

# Example inputs and outputs
s1, wordDict1 = "leetcode", ["leet", "code"]
print(f"Input: s = '{s1}', wordDict = {wordDict1}")
print(f"Output: {wordBreak_optimized(s1, wordDict1)}")  # True

s2, wordDict2 = "applepenapple", ["apple", "pen"]
print(f"Input: s = '{s2}', wordDict = {wordDict2}")
print(f"Output: {wordBreak_optimized(s2, wordDict2)}")  # True

s3, wordDict3 = "catsandog", ["cats", "dog", "sand", "and", "cat"]
print(f"Input: s = '{s3}', wordDict = {wordDict3}")
print(f"Output: {wordBreak_optimized(s3, wordDict3)}")  # False