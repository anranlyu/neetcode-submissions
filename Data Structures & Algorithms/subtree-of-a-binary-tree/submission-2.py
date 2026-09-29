# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        array =""

        def dfs(r):
            nonlocal array
            if r == None:
                array +=" "
                return
            array += str(r.val)
            dfs(r.left)
            dfs(r.right)

        dfs(root)
        array2 = array
        array = ""
        dfs(subRoot)

        return array in array2


        
        