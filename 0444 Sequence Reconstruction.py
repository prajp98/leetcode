def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
    s = set()

    for seq in sequences:
        for i in range(len(seq) - 1):
            s.add((seq[i], seq[i + 1]))
    print(s)
    for i in range(len(nums) - 1):
        if (nums[i], nums[i + 1]) not in s:
            return False
    return True