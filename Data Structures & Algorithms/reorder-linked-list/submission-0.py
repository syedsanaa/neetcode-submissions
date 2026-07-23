# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        f=s=head 
        while f and f.next: 
            f=f.next.next
            s=s.next
        prev=None 
        curr=s.next 
        s.next=None
        while curr: 
            n= curr.next 
            curr.next=prev 
            prev = curr 
            curr=n

        f1=head 
        f2=prev
        while f2 :
            t1,t2=f1.next,f2.next
            f1.next=f2
            f2.next=t1 
            f1=t1 
            f2=t2
            
