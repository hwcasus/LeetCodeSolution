# 378. Kth Smallest Element in a Sorted Matrix
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
# https://github.com/CyC2018/CS-Notes/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3.md#%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        low, high = matrix[0][0], matrix[-1][-1]
        while (low <= high):
            mid = low + (high - low)//2
            
            count = 0
            for row in matrix:
                for n in row:
                    if n <= mid: count+=1
                    
            if count < k: low = mid + 1
            else: high = mid - 1
        
        return low
    
    def kthSmallest1(self, matrix, k):
        low, high = matrix[0][0], matrix[-1][-1]
        while (low < high):
            mid = (low+high)//2
            count = 0
            for row in matrix:
                for n in row:
                    if n <= mid: count+=1

            if count < k: low = mid+1
            else: high = mid
        return low