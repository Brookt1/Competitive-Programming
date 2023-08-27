# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        left,right=head,head
        c=0
        node=head
        while node:
            node=node.next
            c+=1
        val=c-n
        if val==0: return head.next
        if c==1: return None
        node=head
        cc=1
        while node:
            if cc==val:
                node.next=node.next.next
                return head
            cc+=1
            node=node.next

#The below answer is the best that i can found in the leetcode solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         dummy = ListNode(0,head)
#         left, right = dummy, head

#         while n>0 and right:
#             right = right.next
#             n-=1
#         while right:
#             left, right = left.next, right.next
        
#         left.next = left.next.next

#         return dummy.next
