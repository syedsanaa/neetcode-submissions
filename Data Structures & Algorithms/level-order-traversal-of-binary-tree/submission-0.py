# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        q=deque()
        h=defaultdict(list)
        q.append((root,0))
        i=0 
        while q: 
            x,y=q.popleft()
            h[y].append(x.val)
            if x.left:
                q.append((x.left,y+1))
            if x.right: 
                q.append((x.right,y+1))
        return list(h.values())
            

        