def boldWords(self, words: List[str], s: str) -> str:
    bold = [0] * len(s)
    for word in words:
        start = 0
        while start < len(s):
            i = s.find(word, start)
            if i >= 0:
                bold[i:i + len(word)] = [1] * len(word)
                start = i + 1
            else:
                break
    res = []
    for i, c in enumerate(s):
        if bold[i] and (i == 0 or not bold[i - 1]):
            res.append('<b>')
        res.append(c)
        if bold[i] and (i == len(s) - 1 or not bold[i + 1]):
            res.append('</b>')
    return "".join(res)