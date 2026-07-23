"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes={}
        def bacltracking(curr): 
            if not curr: 
               return  None 
            if curr in nodes: 
                return nodes[curr]  
            nodes[curr]=Node(curr.val,None,None)
            nextt=bacltracking(curr.next)
            random=bacltracking(curr.random)
            nodes[curr].next=nextt 
            nodes[curr].random= random 
            return nodes[curr]
        bacltracking(head)
        return nodes[head] if nodes else None 


