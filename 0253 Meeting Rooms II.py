def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    heap = []
    for interval in intervals:
        start, end = interval
        if heap and heap[0] <= start:
            heapq.heappop(heap)  # Reuse the room
        heapq.heappush(heap, end)  # Allocate a new room (or reuse)
    return len(heap)