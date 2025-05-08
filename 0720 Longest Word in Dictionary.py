def longestWord(self, words: List[str]) -> str:
    words.sort()
    s, res = set(), ""
    s.add("")
    for word in words:
        if word[:-1] in s:
            if len(word) > len(res):
                res = word
            s.add(word)
    return res