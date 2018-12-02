# 202. Happy Number
# https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        d = {i:i**2 for i in range(0, 10)}
        
        record = [n]
        
        while n != 1:
            new_n = 0
            while n != 0:
                new_n+=d[n%10]
                n//=10
                
            if new_n in record:
                return False
            else:
                record.append(new_n)
                n = new_n
                
        return True
    
    def isHappy2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def new_number(n):
            total = 0
            while n:
                n,rem = divmod(n,10)
                total += rem ** 2
            return total        
        
        visited = set()

        while True:
            _new = new_number(n)
            if _new == 1:
                return True
            if _new in visited:
                return False
            visited.add(_new)
            n = _new
