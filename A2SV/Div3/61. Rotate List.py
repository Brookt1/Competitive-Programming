# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head: return None
        count=1
        last=head
        while last.next:
            count+=1
            last=last.next
        k=k%count
        last.next=head
        node=head
        for i in range(count-k-1):
            node=node.next
        
        head=node.next
        node.next=None
        return head
