def canMeasureWater(self, x: int, y: int, z: int) -> bool:
    if z > x + y:
        return False
    seen = set()

    def dfs(s):
        if s == z:
            return True
        if s in seen or s < 0 or s > x + y:
            return False
        seen.add(s)
        return dfs(s + x) or dfs(s - x) or dfs(s + y) or dfs(s - y)

    return dfs(0)

def canMeasureWater(self, x: int, y: int, z: int) -> bool:
    if z > x + y:
        return False
    if z == 0:
        return True
    return z % gcd(x, y) == 0