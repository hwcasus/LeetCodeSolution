# 47. Permutations II
# https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        ret = []
        visited = [False]*len(nums)
        
        def go(current):
            if len(current) == len(nums):
                ret.append(current)
                return
            
            for i in range(len(nums)):
                # 如果當前元素 i 跟上一個元素 i-1 相同, 但還沒拜訪過上一個元素
                # 這個情況就會變成 "先取 i 再取 i-1" 和 "先取 i-1 再取 i" 的兩種重複
                # 而前者可以通過下一行的判斷，後者不行
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]: continue
                if visited[i]: continue
                    
                visited[i] = True
                go(current+[nums[i]])
                visited[i] = False
        go([])
        return(ret)
