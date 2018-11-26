# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/description/

class MyQueue:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.in_stack.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.in_to_out()
        return self.out_stack.pop(0)
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.in_to_out()
        return self.out_stack[0]
        
    def in_to_out(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop(0))

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not (self.in_stack or self.out_stack)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()