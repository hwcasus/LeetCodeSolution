# 648. Replace Words
# https://leetcode.com/problems/replace-words/description/

class Solution:
    def replaceWords(self, d, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = {}
        for w in d:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t=t[c]
            t['end']=w
        
        def replace(word, END='end'):
            cur = trie
            for c in word:
                if c not in cur or END in cur: break
                cur = cur[c]
            return cur.get(END, word)
        
        return " ".join(map(replace, sentence.split()))
