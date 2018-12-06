# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0: return True
        if x < 0 or x%10 == 0: return False

        invt_x = 0
        while x > invt_x:
            invt_x = invt_x*10 + x%10
            x //= 10

        return x == invt_x or x == invt_x//10

    def isPalindromeMe(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0: return True
        if x < 0 or x%10 == 0: return False

        # print(x)
        c = x
        invt_x = 0
        while x != 0:
            invt_x *= 10
            invt_x += x%10
            # print(x, invt_x)
            if x == invt_x: return True
            x //= 10

        return c == invt_x
