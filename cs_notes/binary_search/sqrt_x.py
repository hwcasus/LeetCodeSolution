# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/description/

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:return x
        low, high = 0, x
                
        print('low\tmid\thigh')
        while low <= high:
            mid = low + (high - low)//2
            est = mid**2
            if est > x:
                print('{}\t{}\t{}, 答案比 mid 小, 要往左邊走'.format(low, mid, high))
                high = mid -1
            else:
                print('{}\t{}\t{}, 答案比 mid 大, 要往右邊走'.format(low, mid, high))
                low = mid + 1
            
        return low-1
        
    def mySqrtOld(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1: return x
        
        low, high = 1, x
        
        print('low\tmid\thigh')
        while low < high:   
            mid = low + (high - low)//2
            est = mid*mid
            if est > x:
                print('{}\t{}\t{}, 答案比 mid 小, 要往左邊走'.format(low, mid, high))
                high = mid
            else:
                print('{}\t{}\t{}, 答案比 mid 大, 要往右邊走'.format(low, mid, high))
                low = mid + 1
                
        return high -1
