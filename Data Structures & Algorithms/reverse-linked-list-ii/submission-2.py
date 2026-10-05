# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i=1
        slow,fast=head,head 
        prev=None
        while i!=left: 
            prev=slow
            slow=slow.next 
            fast=fast.next 
            i+=1
        prev1=prev 
        start=start1=slow 
        while i<right: 
            slow=slow.next 
            #stop=fast.next 
            fast=fast.next.next
            i+=2 
        #if fast: 
            #stop=fast 
        #reversing 
        i=0
        while i<right-left+1: 
            temp=start.next 
            start.next=prev 
            prev=start 
            start=temp 
            i+=1
        start1.next=start
        if prev1: 
            prev1.next=prev 
            return head
        return prev


            
        
        