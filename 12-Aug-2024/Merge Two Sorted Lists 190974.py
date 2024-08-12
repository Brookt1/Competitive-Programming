# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode()
        node = dummy
        first = list1
        second = list2
        while first and second:
            if first.val < second.val:
                node.next = first
                first = first.next
            else:
                node.next = second
                second = second.next
            node = node.next
        if first:
            node.next = first
        if second:
            node.next = second
        return dummy.next

