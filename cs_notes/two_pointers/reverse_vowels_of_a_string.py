# 345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        h = 0
        e = len(s)-1
        
        VOWELS = "AEIOUaeiou"
        new_s = ['0']*(e+1)
        
        while h <= e:
            if s[h] not in VOWELS:
                new_s[h] = s[h]
                h+=1
            elif s[e] not in VOWELS:
                new_s[e] = s[e]
                e-=1
            else:
                new_s[h] = s[e]
                new_s[e] = s[h]
                h +=1
                e -=1
            
        return ''.join(new_s)