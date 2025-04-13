def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    heap = [(nums1[0] + nums2[0], 0, 0)]
    m, n = len(nums1), len(nums2)
    res = []
    seen = set((0, 0))
    while heap and len(res) < k:
        _, i, j = heapq.heappop(heap)
        res.append([nums1[i], nums2[j]])
        if i + 1 < m and (i + 1, j) not in seen:
            heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            seen.add((i + 1, j))
        if j + 1 < n and (i, j + 1) not in seen:
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            seen.add((i, j + 1))
    return res

def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    minHeap = []

    for i in range(min(k, len(nums1))):
        heapq.heappush(minHeap, (nums1[i] + nums2[0], i, 0))

    ans = []
    while minHeap and len(ans) < k:
        _, i, j = heapq.heappop(minHeap)
        ans.append([nums1[i], nums2[j]])
        if j + 1 < len(nums2):
            heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))

    return ans