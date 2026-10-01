# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    #     output = root
    #     def dfs(r, s,b):
    #         nonlocal output
    #         if r == None:
    #             return
    #         if s.val <= r.val <= b.val:
    #             output = r
    #             return
    #         dfs(r.left,s,b)
    #         dfs(r.right,s,b)
    #     if p.val > q.val:
    #         t = p
    #         p = q
    #         q = t
    #     dfs(root,p,q)
    #     return output
    def lowestCommonAncestor(self, root, p, q):
        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur