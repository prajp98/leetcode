def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    flowerbed = [0] + flowerbed + [0]
    l = len(flowerbed)
    if n == 0:
        return True
    for i in range(1, l - 1):
        if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
            n -= 1
            flowerbed[i] = 1
            if n == 0:
                return True
    return False