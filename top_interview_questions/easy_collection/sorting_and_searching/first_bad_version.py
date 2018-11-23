# First Bad Version
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.first_bad_version_helper(0, n)

    def first_bad_version_helper(self, low, high):
        if low < high:
            mid = low + (high-low)//2
            if not isBadVersion(mid):
                return self.first_bad_version_helper(mid+1, high)
            else:
                return self.first_bad_version_helper(low, mid)
        else:
            return low

    def first_bad_version_helper2(self, low, high):
        while low < high:
            mid = low + (high-low)//2
            if not isBadVersion(mid):
                low = mid+1
            else:
                high = mid
        return low