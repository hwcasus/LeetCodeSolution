# 93. Restore IP Addresses
# https://leetcode.com/problems/restore-ip-addresses/description/

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        ret = []
        def go(current, leftover):
            if len(current) == 4:
                if len(leftover) == 0: ret.append(current)
                return
            for i in range(1, min(4, len(leftover)+1)):
                ## 這裡好像不太像是 backtracking.
                prefix, new_leftover = leftover[-i:], leftover[:-i]
                if int(prefix) > 255: continue
                if prefix[0] == "0" and len(prefix) > 1: continue
                go([prefix] + current, new_leftover)
        
        go([], s)
        return [".".join(ip) for ip in ret]
