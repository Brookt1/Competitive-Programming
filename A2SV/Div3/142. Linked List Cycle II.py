# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hs=set()
        while head:
            if head not in hs:
                hs.add(head)
                head=head.next
            else:
                return head
        return None
        
