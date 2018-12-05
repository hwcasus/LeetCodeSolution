# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        idx = 0
        for chars in zip(*strs):
            if len(set(chars)) != 1: return strs[0][:idx]
            idx += 1
        return strs[0][:idx]

    def longestCommonPrefixMe(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret=""
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                ret += chars[0]
            else:
                return ret
        return ret

    def longestCommonPrefixOld(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        min_s = None
        for s in strs:
            if min_s is None:
                min_s = s
            elif len(s) < len(min_s):
                min_s = s

        for i in range(0, len(min_s)):
            for s in strs:
                if s.split(min_s[:i+1])[0] != '':
                    return min_s[:i]

        return min_s
