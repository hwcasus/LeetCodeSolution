# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        想法如同一般的 two pointers
        以左右兩個 pointer 開始往內縮並紀錄最多的水量
        影響水量的只有兩個 pointer 的間距以及兩個pointer之間比較短的那邊
        所以如果期望看到水量有變高的可能，只有把目前高度比較短的那個pointer移動才有機會
        如果動了長度比較高的，水量只有降低的可能性。
        而如果兩邊等長的話，就隨便挑一邊就好。
        每次移動都計算當前水量 也就是 (右邊-左邊) * 最小值(右邊高度, 左邊高度)
        目前想不到證明方式，可能要用反證吧?
        """
        l, r = 0, len(height)-1
        most = 0

        while l<r:
            w = r-l
            h = min(height[l], height[r])
            most = max(most, w*h)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1

        return most
