# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        q=deque([root])
        res=[]
        depth=0 
        visit=set()
        while q: 
            depth+=1
            temp=[]
            for _ in range(len(q)): 
                node=q.popleft()
                if node.left and node.left not in visit: 
                    q.append(node.left)
                    visit.add(node.left)
                if node.right and node.right not in visit: 
                    q.append(node.right)
                    visit.add(node.right)
                temp.append(node.val)
            if depth%2==0: 
                temp.reverse()
            res.append(temp)
        return res