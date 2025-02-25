"""
Problem: Two Best Non-Overlapping Events

You are given a list of events where each event has a start time, end time, and value.
Your task is to find the maximum sum of values that you can obtain by attending at most two
non-overlapping events.

Example:
Input: events = [[1,3,2], [4,6,5], [2,4,3]]
where each event is [start_time, end_time, value]
Output: 8
Explanation: You can attend events [1,3,2] and [4,6,5] for a total value of 2 + 5 = 7,
or events [2,4,3] and [4,6,5] for a total value of 3 + 5 = 8.
"""

# Approach 1: Brute Force (Check all pairs)
# Time Complexity: O(n²) - we check all possible pairs of events
# Space Complexity: O(1) - we only use a few variables
def maxTwoEventsValueBruteForce(events):
    """
    Brute force approach: Check all possible pairs of events and find the best non-overlapping pair.
    If no valid pair exists, return the maximum value of a single event.
    """
    res = 0
    n = len(events)
    events.sort(key=lambda x: x[0])
    for i in range(n):
        for j in range(i + 1, n):
            if events[i][1] < events[j][0]:
                res = max(res, events[i][2] + events[j][2])
    for i in range(n):
        res = max(res, events[i][2])
    return res


# Approach 2: Heap
# Time Complexity: O(n log n) - dominated by the sorting step
# Space Complexity: O(n) - we create a new sorted array
def maxTwoEventsValueSortAndSearch(events):
    """
    Sort events by end time and then by start time.
    For each event, find the best non-overlapping event that ends before this one starts.
    """
    heap = []
    events.sort()
    res = 0
    maxSoFar = 0
    for start, end, val in events:
        while heap and heap[0][0] < start:
            maxSoFar = max(maxSoFar, heapq.heappop(heap)[1])
        res = max(res, maxSoFar + val, val)
        heapq.heappush(heap, (end, val))
    return res


# Approach 3: Line Sweep (Most Optimized)
# Time Complexity: O(n log n) - sorting the points
# Space Complexity: O(n) - storing the points array
def maxTwoEventsValue(events):
    """
    Line sweep approach: Process events in chronological order.
    Keep track of the maximum value seen so far as we sweep through time.
    """

    points = []
    for start, end, value in events:
        points.append((start, 0, value))  # Start point
        points.append((end, 1, value))  # End point

    points.sort()

    max_value = 0
    max_ended_value = 0

    for time, point_type, value in points:
        if point_type == 0:
            max_value = max(max_value, value + max_ended_value)
        else:
            max_ended_value = max(max_ended_value, value)

    return max_value
