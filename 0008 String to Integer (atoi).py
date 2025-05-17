def myAtoi(self, s: str) -> int:
    i = 0
    n = len(s)
    INT_MAX, INT_MIN = 2 ** 31 - 1, -2 ** 31
    while i < n and s[i] == ' ':
        i += 1
    sign = 1
    if i < n and (s[i] == '+' or s[i] == '-'):
        if s[i] == '-':
            sign = -1
        i += 1
    num = 0
    while i < n and s[i].isdigit():
        num = num * 10 + int(s[i])
        if num * sign < INT_MIN:
            return INT_MIN
        elif num * sign > INT_MAX:
            return INT_MAX
        i += 1
    num *= sign

    return num