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

def numRabbits(self, answers: List[int]) -> int:
    count=Counter(answers)
    total=0
    for n,c in count.items():
        size=n+1
        num=math.ceil(c/size)
        total+=num*size
    return total