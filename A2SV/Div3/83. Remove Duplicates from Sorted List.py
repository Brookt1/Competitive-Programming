# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head:
            node=head.next
        else:
            return None
        headPtr=head
        while node:
            if node.val != headPtr.val:
                headPtr.next,headPtr=node,node
            node=node.next
        headPtr.next=None    
        return head
