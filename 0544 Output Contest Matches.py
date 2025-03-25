def findContestMatch(self, n: int) -> str:
    matches = []
    for i in range(1, n + 1):
        matches.append(str(i))
    while len(matches) > 1:
        new = []
        for i in range(len(matches) // 2):
            new.append("(" + matches[i] + "," + matches[-(i + 1)] + ")")
        matches = new
    return matches[0]