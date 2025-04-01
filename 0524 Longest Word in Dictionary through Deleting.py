def findLongestWord(self, s: str, dictionary: List[str]) -> str:
    res = ""

    def is_subsequence(word):
        i, j = 0, 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                j += 1
            i += 1
        return j == len(word)

    for word in dictionary:
        if is_subsequence(word):
            if len(word) > len(res) or (len(word) == len(res) and word < res):
                res = word
    return res