class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap=defaultdict(list)
        state=[0]*numCourses
        for a,b in prerequisites:
            preMap[a].append(b)
        def dfs(course):
            if state[course]==2:
                return True
            if state[course]==1:
                return False
            state[course]=1
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            state[course]=2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True