def countArrangement(self, n: int) -> int:
    def backtrack(pos, visit):
        if pos > n:
            return 1
        count = 0
        for i in range(1, n + 1):
            if not visit[i] and (i % pos == 0 or pos % i == 0):
                visit[i] = True
                count += backtrack(pos + 1, visit)
                visit[i] = False
        return count

    visit = [False] * (n + 1)
    return backtrack(1, visit)