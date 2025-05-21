def calculate(self, s: str) -> int:
    stack = []
    num = 0
    sign = '+'
    s = s.replace(" ", "")

    for i in range(len(s)):
        char = s[i]
        if char.isdigit():
            num = num * 10 + int(char)
        if not char.isdigit() or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                prev = stack.pop()
                stack.append(int(prev / num))
            sign = char
            num = 0
    return sum(stack)