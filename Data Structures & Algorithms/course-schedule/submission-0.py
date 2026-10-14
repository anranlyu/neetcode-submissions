class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        visiting = set()

        def dfs(c):
            if c in visiting:
                return False
            if graph[c] == []:
                return True
            visiting.add(c)
            for pre in graph[c]:
                if not dfs(pre):
                    return False
            visiting.remove(c)
            graph[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True