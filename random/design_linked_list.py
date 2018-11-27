# https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/
class MyLinkedList:
    
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None
            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.len = 0
        self.head = None
        self.tail = None
        
    def check_len(self):
        depth = 0
        current = self.head
        while current:
            depth += 1
            current = current.next
        return depth
    
    def getNode(self, index):
        if index >= self.len : return None
        current = self.head
        counter = 0
        while index > counter:
            counter += 1
            current = current.next

        return current
    
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        print (self.len, self.check_len(),'get')
        node = self.getNode(index)
        return node.val if node else -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        print (self.len, self.check_len(), 'addAtHead')
        if self.head:
            pre_head = self.head
            self.head = ListNode(val)
            self.head.next = pre_head
        else:
            self.head = self.tail = ListNode(val)
        self.len += 1

            
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        print (self.len, self.check_len(), 'addAtTail')
        if self.tail:
            pre_tail = self.getNode(self.len-1)
            new_tail = ListNode(val)
            pre_tail.next = new_tail
            self.tail = new_tail
        else:
            self.head = self.tail = ListNode(val)
        self.len += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        print (self.len, self.check_len(), 'addAtIndex', index, val)
        if index == 0:
            self.addAtHead(val)
        elif index == self.len:
            self.addAtTail(val)
        else :
            prev_ith_node = self.getNode(index-1)
            if prev_ith_node:class MyLinkedList:
    
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None
            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.len = 0
        self.head = None
        self.tail = None
        
    def check_len(self):
        depth = 0
        current = self.head
        while current:
            depth += 1
            current = current.next
        return depth
    
    def getNode(self, index):
        if index >= self.len : return None
        current = self.head
        counter = 0
        while index > counter:
            counter += 1
            current = current.next

        return current
    
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        print (self.len, self.check_len(),'get')
        node = self.getNode(index)
        return node.val if node else -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        print (self.len, self.check_len(), 'addAtHead')
        if self.head:
            pre_head = self.head
            self.head = ListNode(val)
            self.head.next = pre_head
        else:
            self.head = self.tail = ListNode(val)
        self.len += 1

            
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        print (self.len, self.check_len(), 'addAtTail')
        if self.tail:
            pre_tail = self.getNode(self.len-1)
            new_tail = ListNode(val)
            pre_tail.next = new_tail
            self.tail = new_tail
        else:
            self.head = self.tail = ListNode(val)
        self.len += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        print (self.len, self.check_len(), 'addAtIndex', index, val)
        if index == 0:
            self.addAtHead(val)
        elif index == self.len:
            self.addAtTail(val)
        else :
            prev_ith_node = self.getNode(index-1)
            if prev_ith_node:
                new_node = ListNode(val)
                following_node = prev_ith_node.next
                prev_ith_node.next = new_node
                new_node.next = following_node
                self.len += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        print (self.len, self.check_len(), 'deleteAtIndex', index)
        if self.len > 0 and index < self.len:
            if index == 0:
                self.head = self.head.next
                
            pre_ith_node = self.getNode(index-1)
            if pre_ith_node.next:
                ith_node = pre_ith_node.next
                pre_ith_node.next = ith_node.next
            else:
                pre_ith_node.next = None
                self.tail = pre_ith_node
            self.len -= 1
            
            
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
                new_node = Liclass MyLinkedList:
    
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None
            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.len = 0
        self.head = None
        self.tail = None
        
    def check_len(self):
        depth = 0
        current = self.head
        while current:
            depth += 1
            current = current.next
        return depth
    
    def getNode(self, index):
        if index >= self.len : return None
        current = self.head
        counter = 0
        while index > counter:
            counter += 1
            current = current.next

        return current
    
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        print (self.len, self.check_len(),'get')
        node = self.getNode(index)
        return node.val if node else -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        print (self.len, self.check_len(), 'addAtHead')
        if self.head:
            pre_head = self.head
            self.head = ListNode(val)
            self.head.next = pre_head
        else:
            self.head = self.tail = ListNode(val)
        self.len += 1

            
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        print (self.len, self.check_len(), 'addAtTail')
        if self.tail:
            pre_tail = self.getNode(self.len-1)
            new_tail = ListNode(val)
            pre_tail.next = new_tail
            self.tail = new_tail
        else:
            self.head = self.tail = ListNode(val)
        self.len += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        print (self.len, self.check_len(), 'addAtIndex', index, val)
        if index == 0:
            self.addAtHead(val)
        elif index == self.len:
            self.addAtTail(val)
        else :
            prev_ith_node = self.getNode(index-1)
            if prev_ith_node:
                new_node = ListNode(val)
                following_node = prev_ith_node.next
                prev_ith_node.next = new_node
                new_node.next = following_node
                self.len += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        print (self.len, self.check_len(), 'deleteAtIndex', index)
        if self.len > 0 and index < self.len:
            if index == 0:
                self.head = self.head.next
                
            pre_ith_node = self.getNode(index-1)
            if pre_ith_node.next:
                ith_node = pre_ith_node.next
                pre_ith_node.next = ith_node.next
            else:
                pre_ith_node.next = None
                self.tail = pre_ith_node
            self.len -= 1
            
            
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
                following_node = prev_ith_node.next
                prev_ith_node.next = new_node
                new_node.next = following_node
                self.len += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        print (self.len, self.check_len(), 'deleteAtIndex', index)
        if self.len > 0 and index < self.len:
            if index == 0:
                self.head = self.head.next
                
            pre_ith_node = self.getNode(index-1)
            if pre_ith_node.next:
                ith_node = pre_ith_node.next
                pre_ith_node.next = ith_node.next
            else:
                pre_ith_node.next = None
                self.tail = pre_ith_node
            self.len -= 1
            
            
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)