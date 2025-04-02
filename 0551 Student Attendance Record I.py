def checkRecord(self, s: str) -> bool:
    if s.count('A') >= 2:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2] == "L":
            return False
    return True