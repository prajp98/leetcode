def fractionAddition(self, expression: str) -> str:
    fractions = re.findall('[+-]?\\d+/\\d+', expression)
    n = 0
    d = 1
    for fraction in fractions:
        num, den = map(int, fraction.split('/'))
        n = n * den + num * d
        d *= den
    common = gcd(abs(n), d)
    n //= common
    d //= common
    return f"{n}/{d}"