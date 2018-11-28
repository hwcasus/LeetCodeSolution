# 455. Assign Cookies
# https://leetcode.com/problems/assign-cookies/description/

class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        i = 0
        for size in s:
            if i == len(g): break
            if g[i] <= size : i+=1
                
        return i

