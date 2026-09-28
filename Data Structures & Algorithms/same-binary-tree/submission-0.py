# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        s1,s2 = [], []

        def dfs(r):
            nonlocal s1
            if r == None:
                s1.append(None)
                return None
            s1.append(r.val)
            dfs(r.left)
            dfs(r.right)
        
        dfs(p)
        s2=s1.copy()
        s1 = []
        dfs(q)
        if s1==s2:
            return True
        else:
            return False

            