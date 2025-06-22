class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {}
        for a, b in prerequisites:
            if a not in premap:
                premap[a] = []
            premap[a].append(b)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            dependencies = premap.get(course, None)
            if dependencies is None:
                return True
            visited.add(course)
            for dependency in dependencies:
                if dfs(dependency) is False:
                    return False
            visited.remove(course)  # i haven't visited, if visited means i'm looped
            premap.pop(course)      # popping from prempa, tells we have no dependencies
            return True

        for course in range(numCourses):
            if dfs(course) is False:
                return False
        return True
