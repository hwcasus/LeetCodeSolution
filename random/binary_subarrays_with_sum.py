# 930. Binary Subarrays With Sum
# https://leetcode.com/problems/binary-subarrays-with-sum/description/

class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        這個解法的想法是走過整個 A 的同時，紀錄所有出現過的總和及其出現次數
        然後每次多看一個新的元素時，檢查目前的總合 prev_sum 減掉所需的總和 S 的這個差值
        是否有在之前出現過，如果有就表示 只要把這段拔掉，總和就可以剛好是 S
        而記錄次數的目的就是可以紀錄有幾種不同的拔法
        舉例來說，如果目前到第 i 個元素的總和是 4, 所要找的總和是 3
        因為我走過來的路上只會紀錄 [0:0]~[0:i-1] 的總和，
        所以只要這些總和之間有任何一段的總和是 1就代表
        只要把這段拔掉，我就可以達成 4-1=3 的總和，因此只要查閱過去有紀錄到的總和之中
        出現了幾次總和是 1 的情況，這個次數就是目前能夠達到總合為 3 的次數
        """
        freq = [0] * (len(A)+1)
        freq[0]=1
        prev_sum = 0
        ret = 0
        for a in A:

            prev_sum += a
            # if prev_sum-S > 0:
            ret += freq[prev_sum-S]
            freq[prev_sum]+=1

        return ret
