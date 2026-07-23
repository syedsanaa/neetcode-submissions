# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        s=0 
        out=ListNode(0)
        curr=out 
        prev= None 
        while l1 or l2 : 
            if l1 and l2: 
                s+=l1.val 
                s+=l2.val 
                l1=l1.next 
                l2=l2.next
            elif l1: 
                s+=l1.val 
                l1=l1.next
            elif l2: 
                s+=l2.val 
                l2=l2.next
            curr.next= ListNode(s%10)
            curr=curr.next 
            s=s//10
        if s!=0: 
            curr.next=ListNode(s%10)
        return out.next 



            

        

