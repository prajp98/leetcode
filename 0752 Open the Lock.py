def openLock(self, deadends: List[str], target: str) -> int:
    if "0000" in deadends:
        return -1
    nextMap = {'0': '91', '1': '02', '2': '13', '3': '24', '4': '35', '5': '46', '6': '57', '7': '68', '8': '79',
               '9': '80'}
    visit = set(deadends)
    q = deque(["0000"])
    moves = 0
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            if curr == target:
                return moves
            for i in range(4):
                for j in range(2):
                    nex = curr[:i] + nextMap[curr[i]][j] + curr[i + 1:]
                    if nex not in visit:
                        q.append(nex)
                        visit.add(nex)
        moves += 1
    return -1