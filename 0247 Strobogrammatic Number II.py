def findStrobogrammatic(self, n: int) -> List[str]:
    def build(x):
        if x == 0:
            return [""]
        if x == 1:
            return ["0", "1", "8"]
        middles = build(x - 2)
        res = []
        for mid in middles:
            for pair in [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]:
                if x == n and pair[0] == "0":
                    continue  # Skip numbers with leading zero
                res.append(pair[0] + mid + pair[1])
        return res

    return build(n)