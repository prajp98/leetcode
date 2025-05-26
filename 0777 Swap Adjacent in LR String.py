def canTransform(self, start: str, end: str) -> bool:
    if start.replace("X", "") != end.replace("X", ""):
        return False

    i = j = 0
    n = len(start)

    while i < n and j < n:
        # Skip X in both strings
        while i < n and start[i] == 'X':
            i += 1
        while j < n and end[j] == 'X':
            j += 1

        # If both reached the end, it's valid
        if i == n and j == n:
            return True
        if i == n or j == n:
            return False

        if start[i] != end[j]:
            return False

        if start[i] == 'L' and i < j:
            return False
        if start[i] == 'R' and i > j:
            return False
        i += 1
        j += 1
    return True