# 155. Min Stack
# https://leetcode.com/problems/min-stack/description/

# http://alrightchiu.github.io/SecondRound/stack-neng-gou-zai-o1qu-de-zui-xiao-zhi-de-minstack.html

class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        # Could be solved by using two stack, but python got `tuple`
        # to save (current value, current min value) at the same time.
        self.act_stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        
        min_x = x if not self.act_stack else min(x, self.getMin())
        self.act_stack.append((x, min_x))
        

    def pop(self):
        """
        :rtype: void
        """
        return self.act_stack.pop()[0]
        

    def top(self):
        """
        :rtype: int
        """
        return self.act_stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.act_stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()