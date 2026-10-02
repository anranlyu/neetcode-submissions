# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        counts = 0

        def dfs(node,biggest):
            nonlocal counts
            if node.val >= biggest:
                counts += 1
                biggest = node.val
            if node.left: dfs(node.left, biggest)
            if node.right: dfs(node.right,biggest)
        
        dfs(root,-100)
        return counts
            
