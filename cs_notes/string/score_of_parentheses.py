# 856. Score of Parentheses
# https://leetcode.com/problems/score-of-parentheses/description/

class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        這個解法的想法是括號的深度
        計算深度來區別目前的乘法輛，也就是說
        深度已經決定這層括號內的每個數字要被乘幾次了
        舉例來說 ()(()(()(())))
        先將 () 相連的抽換成 1 就會變成
        1(1(1(1)) -> 1 + (1) + ((1)) + (((1))) -> 1 + 2 + 4 + 8
        而下面的解法是
        當遇到左括號，就往下一層深度, stack 多加一個 0
        當遇到右括號，就退出一層深度，stack.pop(), 而根據當前的數值，這裡分成兩種狀況
            假若 stack.pop() 為 0 那就表示這是一個單獨的(), 在上一層+1
            假若 stack.pop() 大於 0, 就表示這是一個包含其他括號的右括號結尾如 (()()) 的最後一個括號
            這樣的話我就把當前的值*2, 加回到上一層的 stack
        可以看 https://leetcode.com/problems/score-of-parentheses/solution/ 的 solution 2
        """
        stack = [0] # 這很重要
        for s in S:
            # print(stack, s)
            if s == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1]+=max(2*v, 1)

        return stack[0]

    def scoreOfParenthesesFailed(self, S):
        """
        :type S: str
        :rtype: int
        有 Bug, 無法解
        """
        stack = []

        for s in S:
            if stack and s ==')' and stack[-1] =='(':
                stack.pop()
                stack.append('1')
            else:
                stack.append(s)
        print(stack)

        # balance = 0
        # tmp = [0]
        # for op in stack:
        #     if op == '(':
        #         balance+=1
        #         tmp.append[0]
        #     elif op == ')':
        #         balance-=1
        #     else:
        #         tmp[balance] += 1
        #     if balance == 0: pass
        # return score
