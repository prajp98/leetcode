def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
    n = len(intervals)
    starti = sorted((start, i) for i, (start, _) in enumerate(intervals))
    res = []
    for interval in intervals:
        end = interval[1]
        # Binary search for the smallest start >= end
        l, r = 0, n - 1
        i = -1
        while l <= r:
            mid = (l + r) // 2
            if starti[mid][0] >= end:
                i = starti[mid][1]
                r = mid - 1  # Try to find smaller valid start
            else:
                l = mid + 1
        res.append(i)
    return res

def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
    n = len(intervals)
    starti = sorted((start, i) for i,(start,_) in enumerate(intervals))
    res = []
    for interval in intervals:
        end = interval[1]
        # Use binary search to find first start >= end
        i = bisect_left(starti, (end,))
        if i < n:
            res.append(starti[i][1])
        else:
            res.append(-1)
    return res