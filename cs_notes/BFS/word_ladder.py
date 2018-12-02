# 127. Word Ladder
# https://leetcode.com/problems/word-ladder/description/
# https://leetcode.com/problems/word-ladder/discuss/40723/Simple-to-understand-Python-solution-using-list-preprocessing-and-BFS-beats-95

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        def build_dict(w):
            d = {}
            for word in w:
                for i in range(len(word)):
                    s = word[:i] + '_' + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d
        
        visited=set()
        queue = [beginWord]
        d = build_dict(wordList + [beginWord])
        step = 0
        while queue:
            step+=1
            for i in range(len(queue)):
                curr = queue.pop(0)
                if curr == endWord: return step                
                for i in range(len(curr)):
                    s = curr[:i] + '_' + curr[i+1:]
                    for n in d.get(s, []):
                        if n not in visited:
                            queue.append(n)
                            visited.add(n)
        return 0
