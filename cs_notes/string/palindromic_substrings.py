# 647. Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/description/
# https://leetcode.com/problems/palindromic-substrings/discuss/105687/Python-Straightforward-with-Explanation-(Bonus-O(N)-solution)
# https://zh.wikipedia.org/wiki/%E6%9C%80%E9%95%BF%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        這個解法的想法分成2個部分
        1) 走過所有的 substring
        2) 每走過一個 substring, 就確認他是不是回文

        下面的解法將這兩點同時利用，從長度 1 和 2 的 substring 開始
        如果目前的 substring 是回文的，那就將其左右各加一，繼續檢查
        下方迴圈所要走遍所有可能 substring 的中心點
        pp則去檢查說，以目前的中心點往外不斷擴張，可以有幾個 substring
        如此一來就可以涵蓋到所有的 substring, 如果要更仔細地解釋，
        可以想像出所有的 substring 分成奇數長度跟偶數長度, 若假設 s 的長度為 3
        可能的奇數長度 substring 的中心點就一定是第 0, 1 ,2 個元素
        而可能的偶數長度substring 的中心點就一定是 [0:1], [1:2] 的連續元素
        接著我們將這些可能的中心點同時向左右拓展就會得到
            0 : 0
            1 : 1, [0:2]
            2 : 2
            [0:1] : [0:1]
            [1:2] : [1:2]
        如此一來就看完了所有可能的 substring

        """
        def pp(s, i, j):
            cnt = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                # print(s[i:j+1])
                cnt += 1
                i-=1
                j+=1
            return cnt

        cnt = 0
        for i in range(len(s)):
            cnt += pp(s, i, i) + pp(s, i, i+1)

        return cnt


    def countSubstringsDP(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)): dp[i][i] = 1
        for row in range(len(s)-1, -1, -1):
            for col in range(row+1, len(s)):
                if s[row]!=s[col]: continue
                if col == row + 1:
                    dp[row][col] = 1
                else:
                    dp[row][col] = 1 if dp[row+1][col-1]==1 else 0

        return sum([sum(row) for row in dp])


    def countSubstringsSlow(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        def checkIfPalindromic(ss):
            return ss==ss[::-1]


        for i in range(len(s)+1):
            for j in range(i, len(s)+1):
                count += 0 if i == j else int(checkIfPalindromic(s[i:j]))

        return count


    def countSubstringsSuperSlow(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        def checkIfPalindromic(ss):
            l, h = 0, len(ss)-1
            while l < h:
                if ss[l] != ss[h]:
                    return False
                l+=1
                h-=1

            return True


        for i in range(len(s)+1):
            for j in range(i, len(s)+1):
                count += 0 if i == j else int(checkIfPalindromic(s[i:j]))

        return count


    def countSubstringsFailed(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0

        def checker(l, h):
            if l < 0 or h > len(s)-1 or h == l: return 0

            count = 1
            ll, hh = l, h
            while ll < hh:
                if s[ll]!=s[hh]:
                    count = 0
                    break
                else:
                    ll+=1
                    hh-=1

            return count + self.checker(s, l+1, h) + self.checker(s, l, h-1)

        return checker(0, len(s)-1) + len(s)
