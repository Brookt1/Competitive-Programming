# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode()

    def get(self, index: int) -> int:
        node = self.dummy.next
        idx = 0
        while idx < index and node:
            node = node.next
            idx += 1
        if node is None:
            return -1
        return node.val
        
    def addAtHead(self, val: int) -> None:
        nxt = self.dummy.next
        self.dummy.next = ListNode(val, nxt)

    def addAtTail(self, val: int) -> None:
        node = self.dummy
        while node and node.next:
            node = node.next
        node.next = ListNode(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.dummy
        idx = 0
        while idx  < index and  node and node.next:
            node = node.next
            idx += 1
        if idx == index:
            nxt = node.next
            node.next = ListNode(val, nxt)




    def deleteAtIndex(self, index: int) -> None:
        node = self.dummy
        idx = 0
        while idx < index and node:
            node = node.next
            idx += 1
        if node and node.next:
            node.next = node.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)