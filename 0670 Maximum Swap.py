def maximumSwap(self, num: int) -> int:
    digits = list(str(num))
    last = {}
    for i in range(len(digits)):
        last[int(digits[i])] = i

    for i in range(len(digits)):
        for d in range(9, int(digits[i]), -1):
            if last.get(d, -1) > i:
                digits[i], digits[last[d]] = digits[last[d]], digits[i]
                return int("".join(digits))
    return num