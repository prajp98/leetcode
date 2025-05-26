def findCelebrity(self, n: int) -> int:
    # Step 1: Find a candidate
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i

    # Step 2: Verify the candidate
    for i in range(n):
        if i == candidate:
            continue
        if knows(candidate, i) or not knows(i, candidate):
            return -1
    return candidate