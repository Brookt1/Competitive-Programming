# Problem: Sum of Prefix Scores of Strings - https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/


class TrieNode:

    def __init__(self):  
        self.children = [None] * 26
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.children[ord(ch) - ord('a')]:
                node.children[ord(ch) - ord('a')] = TrieNode()
            node.children[ord(ch) - ord('a')].count += 1
            node = node.children[ord(ch) - ord('a')]

    def get_score(self, word):
        node = self.root
        score = 0
        for ch in word:
            score += node.children[ord(ch) - ord('a')].count
            node = node.children[ord(ch) - ord('a')]
        return score
            
        

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = []
        for word in words:
            ans.append(trie.get_score(word))
        
        return ans


        