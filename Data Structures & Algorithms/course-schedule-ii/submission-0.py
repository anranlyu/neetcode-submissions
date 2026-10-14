class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a , b in prerequisites:
            graph[a].append(b)

        seen = set()
        done = set()
        res = deque()

        def dfs(c):
            nonlocal res
            if c in seen:
                return False
            if graph[c] == [] or c in done:
                if c not in res:
                    res.append(c)
                return True
            seen.add(c)
            for pre in graph[c]:
                if not dfs(pre):
                    return False
            seen.remove(c)
            res.append(c)
            done.add(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return list(res)

        
                
            