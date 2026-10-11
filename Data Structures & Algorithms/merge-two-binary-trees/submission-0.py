# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(n1,n2):
            merged = TreeNode()
            n1left = None
            n1right = None
            n2left = None
            n2right = None
            
            if not n1 and not n2:
                return None
            if n1:
                merged.val += n1.val
                n1left = n1.left
                n1right = n1.right
            if n2:
                merged.val += n2.val
                n2left = n2.left
                n2right = n2.right

            merged.left = dfs(n1left,n2left)
            merged.right = dfs(n1right,n2right)

            return merged

        return dfs(root1,root2)


