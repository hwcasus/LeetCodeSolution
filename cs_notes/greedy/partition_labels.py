# 763. Partition Labels
# https://leetcode.com/problems/partition-labels/description/

class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        
        # save last occurrence index of all char in S to a list
        
        def c_to_i(c): return ord(c) - ord('a')
        
        char_idx = [0]* 26 
        for idx, char in enumerate(S):
            char_idx[c_to_i(char)] = idx
        
        ret = []
        
        current = 0
        while current < len(S):
            very_end = current
            # Iterate over the string, check last occurrence index of char and keep update the largest index.
            # if our current index `i` is equal to the largest index we record, it means that we should cut this part out
            # and append its index to the return list.
            for i in range(current, len(S)):
                if i > very_end: break
                very_end = max(very_end, char_idx[c_to_i(S[i])])
            
            ret += [very_end-current+1]
            current = very_end+1
                
        return ret