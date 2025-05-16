def lastRemaining(self, n: int) -> int:
    head, step = 1, 1
    left = True
    while n > 1:
        if left or n % 2 == 1:
            head = head + step
        n = n // 2
        step = step * 2
        left = not left
    return head