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

def findMinDifference(self, timePoints: List[str]) -> int:
    if len(timePoints) > 1440:
        return 0
    seen = [False] * 1440
    for time in timePoints:
        t = int(time[:2]) * 60 + int(time[3:])
        if seen[t]:
            return 0
        seen[t] = True
    prev=first=last=-1
    res=1440
    for i in range(1440):
        if seen[i]:
            if prev!=-1:
                res=min(res,i-prev)
            else:
                first = i
            prev = i
    res=min(res,1440-prev+first)
    return res