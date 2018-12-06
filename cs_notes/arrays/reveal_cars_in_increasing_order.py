# 950. Reveal Cards In Increasing Order
# https://leetcode.com/problems/reveal-cards-in-increasing-order/description/

class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        原本想找出規律，但好像直接反著做最快
        先將原本的值排序，然後每次存一個新的值並將最後一個值擺到第一個
        """
        if not deck: return []

        deck = sorted(deck, reverse=True)
        ret = []
        for n in deck:
            if len(ret): ret.insert(0, ret.pop())
            ret.insert(0, n)

        return ret

