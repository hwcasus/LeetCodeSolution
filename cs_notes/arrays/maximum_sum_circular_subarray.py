# 918. Maximum Sum Circular Subarray
# https://leetcode.com/problems/maximum-sum-circular-subarray/description/

class Solution:
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        請看下一個function解釋
        """
        curr_a = curr_b = 0
        all_max = float('-inf')
        all_min = float('inf')
        for i in range(len(A)):
            curr_a = max(curr_a, 0) + A[i]
            all_max = max(curr_a, all_max)
            curr_b = min(curr_b, 0) + A[i]
            all_min = min(curr_b, all_min)
    
        return all_max if all_max < 0 else max(sum(A)-all_min, all_max)
    
    
    def maxSubarraySumCircularNavie(self, A):
        """
        :type A: List[int]
        :rtype: int
        https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/C++JavaPython-One-Pass
        """
        # 一般狀況
        curr = 0
        all_max = float('-inf')
        for i in range(len(A)):
            curr = max(curr, 0) + A[i]
            all_max = max(curr, all_max)

        # 循環數列狀況, 找最小的且負的連續陣列然後移除掉
        curr = 0
        all_min = float('inf')
        for i in range(len(A)):
            curr = min(curr, 0) + A[i]
            all_min = min(curr, all_min)
        
        case_b = sum(A)-all_min
        return all_max if case_b==0 else max(case_b, all_max)
        
    def maxSubarraySumCircularTooSlow(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        x = [0]+[i+1 for i, a in enumerate(A) if a < 0]
        
        oa = float('-inf')
        for idx in x:
            curr = 0
            for i in range(idx, len(A)+idx):
                curr = max(curr, 0) + A[i%len(A)]
                oa = max(curr, oa)
        
        return oa
