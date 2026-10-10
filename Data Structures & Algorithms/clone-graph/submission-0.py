"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = dict()

        def dfs(n):
            if not n:
                return None
            if n in cloned:
                return cloned[n]
            clone = Node(n.val)
            cloned[n] = clone
            for nb in n.neighbors:
                clone.neighbors.append(dfs(nb))
            return clone
        
        return dfs(node)
        

