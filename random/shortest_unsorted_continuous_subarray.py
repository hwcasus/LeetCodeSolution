# 581. Shortest Unsorted Continuous Subarray
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/

class Solution:
    def findUnsortedSubarray(self, nums):
        """
        monotonic stack 
        ref : https://www.youtube.com/watch?v=8wHH9txAK34
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2: return 0
        right, left = 0, n-1
        
        # monotonic stack 的想法是想辦法維持一個單調遞增/遞減的stack
        # 當新元素要push進來時若是符合遞增/遞減的要求，就扔進去
        # 如果不符合就持續地把stack最上面pop出來，直到新元素丟進去可以符合遞增/遞減的要求
        # 我們在發生pop時去紀錄當時的 index, 就可以去記住亂序的邊界
        
        tmp = []
        for i in range(n):
            # 如果tmp有東西而且新元素會導致遞減(最上層比新元素還大)
            while tmp and nums[tmp[-1]] > nums[i]: left = min(left, tmp.pop())
            tmp.append(i)
                
        tmp = []
        for i in range(n-1, -1, -1):
            # 注意此處為反序，所以新元素應該要比tmp最上層還要小, 
            # 如果tmp有東西而且新元素會導致遞增(最上層比新元素還小)
            while tmp and nums[tmp[-1]] < nums[i]: right = max(right, tmp.pop())
            tmp.append(i)
        
        # 如果原數列就符合遞增要求， left = n-1, right = 0
        # 故要檢查是不是 right > left
        return 0 if right < left else right - left + 1
    
    def findUnsortedSubarrayAmazing(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        right, left = 0, -1
        c_max, c_min = -float('inf'), float('inf')
        
        for i in range(n):
            # 下兩行目標為找出亂序的最右邊邊界，想法是如果目前序列是遞增的，
            # 這表示每次的 c_max 都一定會被更新為 nums[i], 所以如果是遞增數列，則不會更新到 right
            # 相反地，如果 c_max != nums[i], 這表示有比較大的值出現在 i-th 值的左側，也就代表 i 就是目前亂掉的右邊邊界
            c_max = max(nums[i], c_max)
            if c_max != nums[i]: right = i

        for i in range(n-1, -1, -1):
            # 下兩行目標為找出亂序的最左邊邊界，這邊相反的找，想法是如果目前序列是遞增的，反過來則是遞減
            # 這表示每次的 c_min 都一定會被更新為 nums[i], 所以如果是符合遞減，則不會更新到 left
            # 相反地，如果 c_min != nums[i], 這表示我們已經看過比較小的值，而我們只看過 i-th 值的右側，
            # 也就代表 i 就是目前亂掉的左邊邊界
            c_min = min(nums[i], c_min)
            if c_min != nums[i]: left = i
            
        return right - left + 1
        
    def findUnsortedSubarraySort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        is_same = [a==b for a, b in zip(nums, sorted(nums))]
        if all(is_same): return 0
        idx = [i for i, b in enumerate(is_same) if not b]
        return idx[-1] - idx[0] + 1
                
