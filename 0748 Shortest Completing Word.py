def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
    count = defaultdict(int)
    res = ""
    minl = float("inf")
    for ch in licensePlate:
        if ch.isalpha():
            count[ch.lower()] += 1
    for word in words:
        if countWord=Counter(word)
        flag = True
        for ch, c in count.items():
            if c > countWord[ch]:
                flag = False
                break
        if len(word) < minl and flag:
            res = word
            minl = len(word)
    return res