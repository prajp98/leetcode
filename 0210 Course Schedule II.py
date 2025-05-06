def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    res = []
    preMap = defaultdict(list)
    for a, b in prerequisites:
        preMap[a].append(b)
    state = [0] * numCourses

    def dfs(course):
        if state[course] == 2:
            return True
        if state[course] == 1:
            return False
        state[course] = 1
        for nei in preMap[course]:
            if not dfs(nei):
                return False
        state[course] = 2
        res.append(course)
        return True

    for i in range(numCourses):
        if not dfs(i):
            return []
    return res