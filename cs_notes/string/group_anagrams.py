# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            # l = [0]*26
            # for c in s: l[ord(c)-ord('a')]+=1
            # k = "".join(map(str, l))
            k = tuple(sorted(s))
            d.setdefault(k, [])
            d[k].append(s)
        
        return[v for k, v in d.items()]
        
    def groupAnagramsSlow(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        rets=[]
        while strs:
            s_letters = [0]*26
            for c in strs[0]: s_letters[ord(c)-ord('a')]+=1
            
            ret = [0]
            
            for i in range(1, len(strs)):
                table = s_letters.copy()
                if len(strs[0]) != len(strs[i]): continue
                for c in strs[i]:
                    if table[ord(c)-ord('a')] == 0: break
                    table[ord(c)-ord('a')]-=1
                    
                if all(t == 0 for t in table): ret.append(i)
            rets.append([strs.pop(r) for r in ret[::-1]])
            # print(rets)
        return rets
