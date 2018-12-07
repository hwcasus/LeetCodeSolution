# 900. RLE Iterator
# https://leetcode.com/problems/rle-iterator/description/

class RLEIterator:
    # 下面的解法的想法是，只要記錄目前走到第幾步就好了
    # 儲存 A 的時候將連續出現的次數變換成最後一次出現的位置
    # 當 next 被呼叫的時候，將 n 累計起來
    # 然後就只要查閱 n 介於那兩個數字的最後一次出現位置之間
    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.curr = 0
        self.idx = 0
        self.record = []
        c_sum = 0
        for i in range(0, len(A), 2):
            c_sum += A[i]
            if A[i] != 0: self.record.append((c_sum, A[i+1]))

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """

        if self.idx >= len(self.record): return -1

        self.curr+=n
        for count, val in self.record[self.idx:]:
            if self.curr <= count: return val
            self.idx+=1

        return -1



# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
