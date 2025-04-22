def numberOfArithmeticSlices(A: List[int]) -> int:
    count = 0
    for s in range(len(A) - 2):
        d = A[s + 1] - A[s]
        for e in range(s + 2, len(A)):
            if A[e] - A[e - 1] == d:
                count += 1
            else:
                break
    return count
