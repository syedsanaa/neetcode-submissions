# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev=None 
        curr=head
        i=1
        done=False 
        while not done: 
            tleft=curr
            tprev=None 
            while left<=i<=right: #check 
                temp=curr.next
                curr.next=tprev 
                tprev=curr 
                curr=temp
                i+=1
                done=True
            if done: 
                tleft.next=curr 
                if prev: 
                    prev.next=tprev 
                    return head
                else: 
                    return tprev 
            i+=1 
            prev=curr 
            curr=curr.next
            

            
        
        