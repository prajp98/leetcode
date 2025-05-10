def countAndSay(self, n: int) -> str:
    res = "1"
    for _ in range(1, n):
        cur = res
        nex = ""
        count = 1
        for i in range(1, len(cur)):
            if cur[i] == cur[i - 1]:
                count += 1
            else:
                nex += str(count) + cur[i - 1]
                count = 1
        nex += str(count) + cur[-1]
        res = nex
    return res