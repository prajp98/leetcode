def customSortString(self, order: str, s: str) -> str:
    count = Counter(s)
    res = ""
    for ch in order:
        res += ch * count[ch]
        count[ch] = 0
    for ch, freq in count.items():
        if freq != 0:
            res += ch * freq
    return res