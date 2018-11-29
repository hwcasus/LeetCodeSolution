# 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
    
        
        dict_s = {}
        dict_p = {}
        for c in p:
            dict_p.setdefault(c, 0)
            dict_p[c] += 1
            
        offset = len(p)
        chance = len(s) - offset + 1
        ret = []
        for idx in range(chance):
            if not dict_s:
                for c in s[idx:idx+offset]: 
                    dict_s.setdefault(c, 0)
                    dict_s[c]+= 1
            else:
                new_c = s[idx+offset-1]
                old_c = s[idx-1]
                dict_s.setdefault(new_c, 0)
                dict_s.setdefault(old_c, 0)
                dict_s[new_c]+=1
                dict_s[old_c]-=1
                if dict_s[old_c] == 0:
                    del dict_s[old_c]

            # print(s[idx:idx+offset], p, dict_s, dict_p)
            if dict_s == dict_p:
                ret.append(idx)
                
        return ret