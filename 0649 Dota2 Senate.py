def predictPartyVictory(self, senate: str) -> str:
    qr = deque()
    qd = deque()
    n = len(senate)

    for i, ch in enumerate(senate):
        if ch == 'R':
            qr.append(i)
        else:
            qd.append(i)

    while qr and qd:
        r = qr.popleft()
        d = qd.popleft()
        if r < d:
            qr.append(r + n)
        else:
            qd.append(d + n)
    return "Radiant" if qr else "Dire"