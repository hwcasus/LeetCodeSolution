# 374. Guess Number Higher or Lower
# https://leetcode.com/problems/guess-number-higher-or-lower/description/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low <= high:
            mid = low + (high - low)//2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                high = mid
            else:
                low = mid + 1
        
