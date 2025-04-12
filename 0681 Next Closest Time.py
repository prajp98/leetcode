def nextClosestTime(self, time: str) -> str:
    start = int(time[:2]) * 60 + int(time[3:])
    allowed = [int(c) for c in time if c != ':']
    ans = start
    min_diff = 24 * 60

    for i in allowed:
        for j in allowed:
            hour = 10 * i + j
            if hour >= 24:
                continue
            for k in allowed:
                for l in allowed:
                    minute = 10 * k + l
                    if minute >= 60:
                        continue
                    curr = hour * 60 + minute
                    diff = (curr - start) % (24 * 60)
                    if 0 < diff < min_diff:
                        min_diff = diff
                        ans = curr

    return f"{ans // 60:02d}:{ans % 60:02d}"