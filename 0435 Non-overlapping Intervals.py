def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    count = 0
    prevEnd = float('-inf')
    for start, end in intervals:
        if start >= prevEnd:
            prevEnd = end  # No overlap, keep this one
        else:
            count += 1  # Overlap, remove this one
    return count