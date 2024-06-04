# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self, is_end = False):
        self.is_end = is_end
        self.children = {}
class Trie:
    def __init__(self):
        self.root = TrieNode(True)
    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end = True
    def search(self, node, char):
        longest = ''
        for key, obj in sorted(node.children.items()):
            if obj.is_end:
                res = self.search(obj, key)
                if len(res) > len(longest):
                    longest = res
        return char + longest


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        return trie.search(trie.root, '')

