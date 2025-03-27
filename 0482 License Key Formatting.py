def licenseKeyFormatting(self, s: str, k: int) -> str:
    s = s.replace("-", "").upper()
    first = len(s) % k
    res = []
    if first > 0:
        res.append(s[:first])
    for i in range(first, len(s), k):
        res.append(s[i:i + k])
    return "-".join(res)