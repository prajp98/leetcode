def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    for op in tokens:
        if op in "+-*/":
            op2 = stack.pop()
            op1 = stack.pop()
            if op == "+":
                stack.append(op1 + op2)
            elif op == "-":
                stack.append(op1 - op2)
            elif op == "*":
                stack.append(op1 * op2)
            else:
                stack.append(int(op1 / op2))
        else:
            stack.append(int(op))
    return stack[0]
