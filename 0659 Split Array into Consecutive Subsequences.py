def isPossible(self, nums: List[int]) -> bool:
    sub = defaultdict(int)
    count = Counter(nums)
    for num in nums:
        if count[num] == 0:
            continue
        if sub[num - 1] > 0:
            sub[num - 1] -= 1
            sub[num] += 1
        elif count[num + 1] > 0 and count[num + 2] > 0:
            sub[num + 2] += 1
            count[num + 1] -= 1
            count[num + 2] -= 1
        else:
            return False
        count[num] -= 1
    return True