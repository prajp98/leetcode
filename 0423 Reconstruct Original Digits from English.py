def originalDigits(self, s: str) -> str:
    count = Counter(s)
    digits = [0] * 10

    digits[0] = count['z']
    digits[2] = count['w']
    digits[4] = count['u']
    digits[6] = count['x']
    digits[8] = count['g']

    digits[1] = count['o'] - digits[0] - digits[2] - digits[4]
    digits[3] = count['h'] - digits[8]
    digits[5] = count['f'] - digits[4]
    digits[7] = count['v'] - digits[5]
    digits[9] = count['i'] - digits[5] - digits[6] - digits[8]

    result = []
    for num in range(10):
        result.append(str(num) * digits[num])

    return "".join(result)