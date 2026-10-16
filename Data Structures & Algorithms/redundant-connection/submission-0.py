class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = list(range(n+1))
        rank = [1]* (n+1)

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(a,b):
            ra , rb = find(a), find(b)
            if ra == rb:
                return False
            if rank[ra] < rank[rb]:
                ra , rb = rb ,ra
            parents[rb] = parents[ra]
            rank[ra] += rank[rb]
            return True

        for a, b in edges:
            if not union(a,b):
                return [a,b]
        return []