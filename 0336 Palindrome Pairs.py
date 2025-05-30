def palindromePairs(self, words: List[str]) -> List[List[int]]:
    res = []
    m = {word[::-1]: i for i, word in enumerate(words)}
    for i, word in enumerate(words):
        if "" in m and word != "" and word == word[::-1]:
            res.append([i, m[""]])
        for j in range(1, len(word) + 1):
            l = word[:j]
            r = word[j:]
            if l in m and m[l] != i and r == r[::-1]:
                res.append([i, m[l]])
            if r in m and m[r] != i and l == l[::-1]:
                res.append([m[r], i])
    return res