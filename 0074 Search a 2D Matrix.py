def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    u, d = 0, rows - 1
    while u <= d:
        mid = (u + d) // 2
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            break
        elif target > matrix[mid][-1]:
            u = mid + 1
        else:
            d = mid - 1
    l, r = 0, cols - 1
    while l <= r:
        m = (r + l) // 2
        if matrix[mid][m] == target:
            return True
        elif matrix[mid][m] > target:
            r = m - 1
        else:
            l = m + 1
    return False