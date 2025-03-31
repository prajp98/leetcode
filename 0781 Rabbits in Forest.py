def numRabbits(self, answers: List[int]) -> int:
    dic = defaultdict(int)
    res = 0
    for ans in answers:
        if ans == 0:
            res += 1
            continue
        if dic[ans] == 0 or dic[ans] == ans + 1:
            dic[ans] = 1
            res += ans + 1
        else:
            dic[ans] += 1
    return res