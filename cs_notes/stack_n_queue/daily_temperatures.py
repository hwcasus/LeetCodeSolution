# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/description/

class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        num_days = len(T)
        ans = [0]*num_days
        stack = []
        
        # list as stack:
        #   append as push
        #   list[-1] as top
        #   pop as pop
        
        for idx in range(0, num_days):
            while stack and T[stack[-1]] < T[idx]:
                prev_idx = stack.pop()
                ans[prev_idx] = idx - prev_idx
                
            stack.append(idx)
            # print(*ans, *stack)
        
        return ans