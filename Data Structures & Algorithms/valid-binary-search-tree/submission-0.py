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
        if not root.left and not root.right: 
            return True 
        def dfs(stack,limits): 
            while stack:
                node=stack.pop ()
                if node.left: 
                    stack.append(node.left)
                    limits[node.left]=[limits[node][0],node.val] # NON INCLUSIVE LIMITS 
                    if node.left.val>=node.val or node.left.val<=limits[node][0]: 
                        return False 
                if node.right: 
                    stack.append(node.right)
                    limits[node.right]=[node.val,limits[node][1]] # NON INCLUSIVE LIMITS 
                    if node.right.val<=node.val or node.right.val>=limits[node][1]: 
                        return False 
            return True 
        limits=defaultdict(list)
        limits[root]=[float('-inf'),float('inf')]
        stack=[]
        stack.append(root)
        if dfs(stack,limits): 
            return True
        else: 
            return False 



        