# 537. Complex Number Multiplication
# https://leetcode.com/problems/complex-number-multiplication/description/

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # a_i, a_c = a.split('+')
        # a_i, a_c = int(a_i), int(a_c[:-1])
        # b_i, b_c = b.split('+')
        # b_i, b_c = int(b_i), int(b_c[:-1])
        
        a_i, a_c = map(int, a[:-1].split('+'))
        b_i, b_c = map(int, b[:-1].split('+'))      
        return "{}+{}i".format(str(a_i*b_i - a_c*b_c), str(a_i*b_c + b_i*a_c))
