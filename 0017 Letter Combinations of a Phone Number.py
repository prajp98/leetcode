def letterCombinations(self, digits: str) -> List[str]:
    res = []
    if not digits:
        return []
    digitToChar = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def dfs(i, s):
        if i == len(digits):
            res.append(s)
            return
        letters = digitToChar[digits[i]]
        for c in letters:
            dfs(i + 1, s + c)

    dfs(0, "")
    return res