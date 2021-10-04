# https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.super_head = Node(float('inf'))
        self.super_tail = Node(float('-inf'))
        self.super_head.next = self.super_tail
        self.super_tail.prev = self.super_head
        self.length = 0


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.length or index < 0:
            return -1

        ptr = self.super_head
        for i in range(-1, index):
            ptr = ptr.next

        return ptr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        first_node = self.super_head.next
        new_node = Node(val, first_node, self.super_head)
        first_node.prev = new_node
        self.super_head.next = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        last_node = self.super_tail.prev
        new_node = Node(val, self.super_tail, last_node)
        last_node.next = new_node
        self.super_tail.prev = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == self.length:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            ptr = self.super_head
            for i in range(index):
                ptr = ptr.next

            next_ptr = ptr.next
            new_node = Node(val, next_ptr, ptr)
            next_ptr.prev = new_node
            ptr.next = new_node

            self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index < self.length:

            ptr = self.super_head
            for i in range(-1, index):
                ptr = ptr.next

            ptr.next.prev = ptr.prev
            ptr.prev.next = ptr.next
            self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)