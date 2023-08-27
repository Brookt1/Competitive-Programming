# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        leftNode,midNode,rightNode=ListNode(),None,ListNode()
        leftPtr,rightPtr,midPtr=leftNode,rightNode,midNode

        n=1
        node=head
        while node:
            nxt=node.next
            if n<left:
                leftPtr.next,leftPtr=node,node
            elif n<=right:
                if n==left: midPtr=node
                node.next=midNode
                midNode=node
            else:
                rightPtr.next,rightPtr=node,node
            node=nxt
            n+=1
        leftPtr.next=midNode
        if midPtr: midPtr.next=rightNode.next

        return leftNode.next
