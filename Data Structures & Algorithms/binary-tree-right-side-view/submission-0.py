# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=deque()
        q.append((root,0))
        d={}
        while q: 
            node,depth=q.popleft()
            if node:
                if depth not in d: 
                    d[depth]=node.val
                q.append((node.right,depth+1))
                q.append((node.left,depth+1))
        return list(d.values())
