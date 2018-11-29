# 605. Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/description/

class Solution:
    def canPlaceFlowersEvenSlow(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        num_bed = len(flowerbed)
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        
        count = 0
        for idx in range(1, num_bed+1):
            print(flowerbed[idx-1:idx+2])
            if sum(flowerbed[idx-1:idx+2]) == 0:
                flowerbed[idx] = 1
                count += 1

        return count==n
        
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if not n: return True
        
        count = 0
        for idx, bed in enumerate(flowerbed):
            if count == n: return True
            if bool(bed): continue
            
            prv = bool(flowerbed[idx-1] if idx > 0 else 0)
            nxt = bool(flowerbed[idx+1] if idx < len(flowerbed)-1 else 0)
            
            if not prv and not nxt:
                flowerbed[idx] = 1
                count +=1 
                
        return count == n