"""
Count and Say

https://leetcode.com/problems/count-and-say/

The count-and-say sequence is the sequence of integers with the first five terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

    Input: 1
    Output: "1"

Example 2:

    Input: 4
    Output: "1211"
"""

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        s = self.countAndSay(n-1)
        tmp_char, tmp_count = [], []
        r = ""
        
        for i, c in enumerate(s):
            if len(tmp_char) > 0:
                if c == tmp_char[-1]:
                    tmp_count[-1] += 1
                else:
                    tmp_char += [c]
                    tmp_count += [1]
            else:
                tmp_char += [c]
                tmp_count += [1]
        
        for char, count in zip(tmp_char, tmp_count):
            r+="{}{}".format(count,char)
        
        return r