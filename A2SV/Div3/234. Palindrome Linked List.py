# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        n=0
        node=head
        while node:
            n+=1
            node=node.next
        half=None
        
        node=head
        c=0

        while node:
            nxt=node.next
            if c==n//2:
                node.next=half
                half=node
            else:
                c+=1
            node=nxt

        while half:
            if head.val!=half.val:
                return False
            head=head.next
            half=half.next

        return True
