# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find(root): 
            if not root: 
                return None 
            if root.val==key: 
                return (insert(root.right,root.left) if root.left else root.right)
            elif root.val>key: 
                root.left=find(root.left) 
            elif  root.val<key: 
                root.right=find(root.right)
            return root
        
        def insert(right,left): 
            if not right: 
                return left
            if right.val>left.val: 
                right.left=insert(right.left,left)
            else: 
                right.right=insert(right.right,left)
            return right
        return find(root)