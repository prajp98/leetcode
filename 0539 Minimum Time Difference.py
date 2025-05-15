def findMinDifference(self, timePoints: List[str]) -> int:
    times = []
    for time in timePoints:
        hours = int(time[:2])
        mins = int(time[3:])
        times.append(hours * 60 + mins)
    times.sort()
    res = float('inf')
    for i in range(len(times) - 1):
        res = min(res, times[i + 1] - times[i])
    res = min(res, 1440 + times[0] - times[-1])
    return res