# Fizz Buzz
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/743/

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        for idx, num in enumerate(range(1, n+1)):
            term = ""
            if (idx+1)%3 == 0:
                term+="Fizz"
            if (idx+1)%5 == 0:
                term+="Buzz"
            
            output.append(term if len(term)>0 else str(num))
                    
        return output