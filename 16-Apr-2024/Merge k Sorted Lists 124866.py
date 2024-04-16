# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        temp = dummy

        for i in range(len(lists)):
            node = lists[i]
            if node:
                heappush(heap, [node.val, i])
        while heap:
            val, idx = heappop(heap)
            temp.next = ListNode(val)
            temp = temp.next
            if lists[idx].next:
                heappush(heap, [lists[idx].next.val, idx])
                lists[idx] = lists[idx].next
        return dummy.next

