def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # Stack O(m+n)
    stack, res, hashmap = [], [], {}
    for num in nums2:
        while stack and num > stack[-1]:
            x = stack.pop()
            hashmap[x] = num
        stack.append(num)
    for n in nums1:
        res.append(hashmap.get(n, -1))
    return res