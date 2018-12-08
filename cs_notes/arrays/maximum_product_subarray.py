# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/description/

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        這個做法非常好懂
        其實最重要的就是負數還有0
        先討論負數，而且必須是奇數個負數，如果是偶數個負數的話會負負得正
        假設數列中有3個負數，則最大值必定存在以三個負數的其中一個作為分割點的左數列或右數列其中一個
        舉例來說 數列是 [2, 2, -3, 2, 2, -4, 2, 2, -5, 2, 2]
        若取-3為分割點則左右分別為 [2 2] [-3] [2 2 -4 2 2 -5 2 2]
        若取-4為分割點則左右分別為 [2 2 -3 2 2] [-4] [2 2 -5 2 2]
        若取-5為分割點則左右分別為 [2 2 -3 2 2 -4 2 2] [-5] [2 2]
        以這個例子的話 最大會是-3分割的右邊
        而使用下面方法的左右各pass一次，這三種分割方式的六個子數列都可以考慮到
        接著我們再來考慮 0, 因為只要經過 0 結果就一定是 0
        這邊的想法可以看做是，把0當成分割點，同時考慮左右側的最大值
        所以將 p 重設為 1, 而因為 p 會先 *= n 所以也不用擔心說 0 這個值不會被比較到
        雖然這個方法是 O(n**2), 但是我覺得好懂多了
        """
        p = 1
        c_max = float('-inf')
        for n in nums:
            p*=n
            c_max = max(c_max, p)
            if n==0: p=1
        p = 1
        for n in nums[::-1]:
            p*=n
            c_max = max(c_max, p)
            if n==0: p=1
        
        return c_max
        
    def maxProductDP(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        之所以要用雙 dp array 似乎是因為考慮ith元素之後的最大值, 一定是來自於
        1) i-1 最小值 * i (可能是負負得正)
        2) i-1 最大值 * i (正常考慮就是這樣)
        3) i 元素 (例如 i-1 最大是 -4, 最小是 -14, 而元素 i 則是 10->這樣取 10 反而最大
        所以每次加入一個新的值，都要比叫這三者去更新 最小跟最大值
        """
        
        dp_min = [nums[0]] + [0]*(len(nums)-1)
        dp_max = [nums[0]] + [0]*(len(nums)-1)
        ret = nums[0]
        for i in range(1, len(nums)):
            cand_a = dp_min[i-1]*nums[i]
            cand_b = dp_max[i-1]*nums[i]
            dp_min[i] = min(nums[i], cand_a, cand_b)
            dp_max[i] = max(nums[i], cand_a, cand_b)
            ret = max(ret, dp_max[i])
        
        return ret
        
