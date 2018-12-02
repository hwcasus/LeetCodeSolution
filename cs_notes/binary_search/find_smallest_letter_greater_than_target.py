# 744. Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

class Solution:
    def nextGreatestLetter(self, letters, target):
        """ 
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left, right = 0, len(letters)-1
        
        while left < right: #when left = right -1, break
            mid = left + (right-left)//2
            if ord(letters[mid]) <= ord(target):
                left = mid + 1
            else:
                right = mid
        
        # 可以想像成找出在 letters 中比 target 還大的最小英文字, 找不到就回傳letters[0]
        return letters[0] if target >= letters[-1] else letters[left]
