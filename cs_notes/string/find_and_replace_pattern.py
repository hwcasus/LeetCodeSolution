# 890. Find and Replace Pattern
# https://leetcode.com/problems/find-and-replace-pattern/description/

class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """

        def compare(a, b):
            # Completely Same Idea of # 205. Isomorphic Strings
            if len(a)!=len(b): return False
            rec_a = [-1]*26
            rec_b = [-1]*26
            for i in range(len(a)):
                ax = ord(a[i])-ord('a')
                bx = ord(b[i])-ord('a')
                if rec_a[ax] == rec_b[bx]:
                    rec_a[ax] = rec_b[bx] = i
                else:
                    return False
            return True

        return [w for w in words if compare(w, pattern)]

