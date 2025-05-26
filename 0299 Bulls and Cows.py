def getHint(self, secret: str, guess: str) -> str:
    bulls = cows = 0
    sc = Counter()
    gc = Counter()

    for s, g in zip(secret, guess):
        if s == g:
            bulls += 1
        else:
            sc[s] += 1
            gc[g] += 1

    for ch in gc:
        cows += min(sc[ch], gc[ch])

    return str(bulls) + "A" + str(cows) + "B"