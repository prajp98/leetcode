def diffWaysToCompute(self, expression: str) -> List[int]:
    memo = {}

    def helper(expr):
        if expr in memo:
            return memo[expr]
        if expr.isdigit():
            return [int(expr)]
        res = []
        for i, ch in enumerate(expr):
            if ch in "+-*":
                left = helper(expr[:i])
                right = helper(expr[i + 1:])
                for l in left:
                    for r in right:
                        if ch == '+':
                            res.append(l + r)
                        elif ch == '-':
                            res.append(l - r)
                        elif ch == '*':
                            res.append(l * r)
        memo[expr] = res
        return res

    return helper(expression)