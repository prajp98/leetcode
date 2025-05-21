def multiply(self, num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    n, m = len(num1), len(num2)
    res = [0] * (n + m)

    for i in reversed(range(n)):
        for j in reversed(range(m)):
            mul = int(num1[i]) * int(num2[j])
            p1, p2 = i + j, i + j + 1
            total = mul + res[p2]

            res[p2] = total % 10
            res[p1] += total // 10
    result = []
    for digit in res:
        if not result and digit == 0:
            continue
        result.append(str(digit))

    return ''.join(result) if result else "0"