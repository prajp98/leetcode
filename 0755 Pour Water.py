def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
    for i in range(volume):
        poured = False
        for dx in [-1, 1]:
            cur = best = k
            # Walk in the direction while the next cell is not higher
            while 0 <= cur + dx < len(heights) and heights[cur + dx] <= heights[cur]:
                if heights[cur + dx] < heights[cur]:
                    best = cur + dx
                cur += dx
            # If we found a lower spot, pour water there
            if best != k:
                heights[best] += 1
                poured = True
                break

        if not poured:
            heights[k] += 1
    return heights