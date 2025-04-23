def maxDistance(self, arrays: List[List[int]]) -> int:
    maxi = 0
    gmin = arrays[0][0]
    gmax = arrays[0][-1]
    for i in range(1, len(arrays)):
        cmin = arrays[i][0]
        cmax = arrays[i][-1]
        maxi = max(maxi, abs(cmax - gmin), abs(gmax - cmin))
        gmin = min(gmin, cmin)
        gmax = max(gmax, cmax)
    return maxi