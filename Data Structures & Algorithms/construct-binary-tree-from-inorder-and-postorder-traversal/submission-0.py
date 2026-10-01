# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(ino,poo): 
            if not ino and not poo: 
                return None 
            root=TreeNode(poo[-1])
            i=ino.index(root.val)
            root.left=build(ino[0:i],poo[0:i])
            root.right=build(ino[i+1:],poo[i:-1])
            return root 
        return build(inorder,postorder)