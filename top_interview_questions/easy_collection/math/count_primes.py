#  ount Primes
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 2:
            return 0
        
        is_prime = [1]*n
        is_prime[0], is_prime[1] = 0, 0
        
        for i in range(2, int(n**0.5)+1):
            if is_prime[i]:
                is_prime[i*i::i] = [0] * len(is_prime[i*i::i])
        
        return sum(is_prime)
        
        