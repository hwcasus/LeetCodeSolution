# 406. Queue Reconstruction by Height
# https://leetcode.com/problems/queue-reconstruction-by-height/description/

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        people.sort(key=lambda x:(-x[0], x[1])) 
        new_people = []
        
        for h, k in people:
            new_people.insert(k, [h, k])
        
        return new_people
