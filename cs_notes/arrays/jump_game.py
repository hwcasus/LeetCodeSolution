# 55. Jump Game
# https://leetcode.com/problems/jump-game/description/

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        這個做法的想法是從終點往回看每一個格子是不是有機會走到終點
        如果有機會，就將p更新到那個位子
        然後再繼續往回看每一個剩下的格子能不能走到更新後的p點
        如果到最後 p 點被更新到 0, 也就是起點
        就表示這個是可以從起點走到終點的, 所以最後是回傳 p == 0
        """

        p = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i+nums[i] >= p: p = i
        return p==0
    
    def canJumpSlow(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reachable = [True]+[False]*(len(nums)-1)
        for i, n in enumerate(nums):
            if reachable[i]:
                for j in range(i, min(len(nums), i+n+1)): 
                    reachable[j]=True
        
        return reachable[-1]
                    
    def canJumpFailed(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        有夠接近，只差反過來檢查 damn
        真的可惜 判斷式幾乎寫對了 damn
        """
        if not nums: return False
        if len(nums)==1: return True
        if nums[0] == 0: return False
        
        for i, n in enumerate(nums[:-1]):
            if (i+n) >= len(nums)-1: return True
        return False
