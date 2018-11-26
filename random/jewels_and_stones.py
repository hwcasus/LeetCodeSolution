# 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ret = 0
        for stone in S:
            ret += int(stone in J)
        return ret