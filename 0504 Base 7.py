def convertToBase7(self, num: int) -> str:
    if num == 0:
        return '0'
    neg = num < 0
    num = abs(num)
    res = ""

    while num > 0:
        digit = num % 7
        res = str(digit) + res
        num //= 7
    if neg:
        res = "-" + res
    return res