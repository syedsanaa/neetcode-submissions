# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res=root.val
        def dfs(root): 
            if not root: 
                return 0

            Leftmax=dfs(root.left)
            Rightmax=dfs(root.right)
            Leftmax=max(Leftmax,0)
            Rightmax=max(Rightmax,0)

            self.res=max(self.res,root.val+Leftmax+Rightmax)
            return root.val+max(Leftmax,Rightmax)
        dfs(root)
        return self.res

