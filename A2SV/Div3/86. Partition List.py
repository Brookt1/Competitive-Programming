# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        lessX=ListNode()
        tail_lessX=lessX

        moreX=ListNode()
        tail_moreX=moreX

        while head:
            if head.val<x:
                tail_lessX.next, tail_lessX=head,head
            else:
                tail_moreX.next, tail_moreX=head,head
            head=head.next
        tail_moreX.next=None
        tail_lessX.next=moreX.next
        
        return lessX.next

