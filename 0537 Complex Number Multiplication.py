def complexNumberMultiply(self, num1: str, num2: str) -> str:
    a, b = num1[:-1].split("+")
    c, d = num2[:-1].split("+")
    a, b, c, d = int(a), int(b), int(c), int(d)
    res = ""
    res = str(a * c - b * d) + "+" + str(a * d + b * c) + "i"
    return res