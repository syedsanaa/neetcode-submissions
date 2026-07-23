# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True 
        def dfs(root,minl,maxl): 
            if root.val<minl or root.val>maxl: 
                return False 
            a=True 
            b=True 
            if root.right: 
                a=dfs(root.right,root.val+1,maxl) # min max are inclusive 
            if root.left: 
                b=dfs(root.left,minl,root.val-1) # min max are inclusive
            return (a and b)
        return dfs(root,float('-inf'),float('inf'))
        