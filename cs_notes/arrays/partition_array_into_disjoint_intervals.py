# 915. Partition Array into Disjoint Intervals
# https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/

ass Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        這個解法的想法是去紀錄三個數值
        1) 目前分割點
        2) 目前分割點左側最大值
        3) 目前最大值
        每次看一個新的元素就要更新目前最大值
        接著檢查目前左側最大值是不是有大過新看到的值，此處可以分成兩個情況來來分析
            a) 如果這個值比左側最大值還要小，那他必須是在分割點的左側，所以要更新目前分割點至目前的位子
               此外，因為分割點被更新目前的元素, 所以左側最大值也必須被更新為當前最大值
            b) 如果這個值比左側最大值還大，他應該在分割點右側，符合目前狀況
        """

        leftmax = currmax = A[0]
        p_idx = 0
        for i, a in enumerate(A):
            currmax = max(currmax, a)
            if leftmax > a:
                p_idx = i
                leftmax = currmax

        return p_idx+1


    def partitionDisjointMe(self, A):
        """
        :type A: List[int]
        :rtype: int
        要找某個idx開始，左側的最大值 < 右側的最小值, 而此 idx 要越小越好
        """

        l_max = [float('-inf')]
        r_min = [float('inf')]

        for i in range(0, len(A)-1):
            l_max.append(max(l_max[-1], A[i]))
            r_min.append(min(r_min[-1], A[len(A)-i-1]))

        for i in range(1, len(l_max)):
            if l_max[i] <= r_min[-i]: return i
