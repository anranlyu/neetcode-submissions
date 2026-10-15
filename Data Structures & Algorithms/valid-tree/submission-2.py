class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()
        done = set()

        def dfs(c, p):
            if c in seen:
                return False
            if c in done:
                return True
            seen.add(c)
            for nb in graph[c]:
                if nb != p:
                    if not dfs(nb, c):
                        return False
            seen.remove(c)
            done.add(c)
            return True

        return dfs(0, None) and len(done) == n

