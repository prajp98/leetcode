def letterCombinations(self, digits: str) -> List[str]:
    res = []
    hashMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "qprs",
        "8": "tuv",
        "9": "wxyz",
    }
    curr = ""

    def dfs(i, curr):
        if len(curr) == len(digits):
            res.append(curr)
            return
        for c in hashMap[digits[i]]:
            dfs(i + 1, curr + c)

    dfs(0, "")
    if digits:
        return res