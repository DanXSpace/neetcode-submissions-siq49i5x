class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            if crs not in adjList:
                adjList[crs] = []
            if pre not in adjList:
                adjList[pre] = []
            adjList[crs].append(pre)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            
            if adjList[crs] == []:
                return True
            
            visit.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False

            visit.remove(crs)
            adjList[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True