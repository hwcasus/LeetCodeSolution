# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/description/

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        使用方塊法, 可以看 solution 3
        或 https://leetcode.com/problems/task-scheduler/discuss/104507/Python-Straightforward-with-Explanation
        可以分成兩種情況討論
        1. 休息時間太短，工作種類太多，也就是可以一直做不一樣的工作都不用休息
           這種狀況就是 task 的數量決定工作的總 intervals 數
        2. 休息時間太長，工作種類太少，也就是每種工作都做過還是需要休息
           這種狀況下，所有工作中數量最大的工作會影響休息的次數
           令 k = 最大工作量, 你至少需要休息 k 次才有機會在第 k 輪做完最後一次的工作
           基於這點我們就可以確定至少需要 (n+1) * (k-1) 的intervals (n+1 是因為休息兩次代表第三次才能再執行該工作)
           除此之外，假設最大工作量 k 的工作種類不只一種(但必定小於 n 種，不然就是狀況1)，
           那麼我們就還需要在第 k 輪時把最後的工作做完，而最後的工作數量 = 工作量為k的工作種類
           所以就得到 (n+1) * (k-1) + (數量為 k 的工作種類)

        基於兩種狀況我們就可以得到 max(len(task), (n+1) * (k-1) + (數量為 k 的工作種類))
        """
        import collections
        task_cnt = list(collections.Counter(tasks).values())
        # k = task_cnt.most_common(1)[0][1]
        k = max(task_cnt)
        final = task_cnt.count(k)
        return max(len(tasks), (n+1)*(k-1)+final)


    def leastIntervalMe(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        雖然很慢但是可行
        amound_cd 可以透過 Counter 去實作
        然後再用 list 紀錄 CD 就可以
        """
        amount_cd = [[0 for _ in range(2)] for _ in range(26)]
        for t in tasks: amount_cd[ord(t)-ord('A')][0]+=1
        sorted(amount_cd, reverse=True)
        task_kind = len(set(tasks))
        amount_cd = amount_cd[:task_kind]


        rest_tasks = len(tasks)
        idx = 0
        while rest_tasks > 0:
            for i in range(len(amount_cd)):
                if amount_cd[i][0] > 0 and amount_cd[i][1] <= idx:
                    # print(idx, 'consume task {}, rest:{}'.format(i, amount_cd[i]))
                    amount_cd[i][0]-=1
                    amount_cd[i][1]+=n+1
                    rest_tasks -= 1
                    break
            idx += 1
        return idx




