def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x: x[1])
    if not intervals:
        return True
    prevEnd = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < prevEnd:
            return False
        prevEnd = intervals[i][1]
    return True