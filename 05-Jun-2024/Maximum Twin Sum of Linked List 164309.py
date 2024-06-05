# Problem: Maximum Twin Sum of Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        


        n = 0
        fast = head
        while  fast and fast.next:
            fast = fast.next.next
            n += 2
        idx = 0
        dic = {}
        node = head
        while node:
            if idx >= n // 2:
                dic[n - 1 - idx] += node.val
            else:
                dic[idx] = node.val
            idx += 1
            node = node.next

        return max(dic.values())

