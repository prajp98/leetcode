def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x: x[1])
    if not intervals:
        return True
    prevEnd = intervals[0][1]
    for interval in intervals[1:]:
        if interval[0] < prevEnd:
            return False
        prevEnd = interval[1]
    return True