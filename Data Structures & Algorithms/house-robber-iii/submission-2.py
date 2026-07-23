# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp={}
        def dfs(root): 
            if not root: 
                return 0 
            if root in dp: 
                return dp[root]
            res1=dfs(root.left)+dfs(root.right) # dont include root 
            res2=root.val 
            if root.left and root.right:
                res2+=dfs(root.left.left)+dfs(root.left.right)+dfs(root.right.left)+dfs(root.right.right)
            elif root.left: 
                res2+=dfs(root.left.left)+dfs(root.left.right)
            elif root.right:
               res2+=dfs(root.right.left)+dfs(root.right.right)
            res=max(res1,res2)
            dp[root]=res
            return res 
        return dfs(root)
