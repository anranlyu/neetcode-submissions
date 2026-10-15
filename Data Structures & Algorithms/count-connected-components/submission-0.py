class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen = set()

        def dfs(c):
            nonlocal seen
            if c in seen:
                return
            seen.add(c)
            for nb in graph[c]:
                    dfs(nb)
            
        component = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                component += 1
        return component
