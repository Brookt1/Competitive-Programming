# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            key = ord(ch) - ord('a')
            if cur.children[key] is None:
                cur.children[key] = TrieNode()
            cur = cur.children[key]
        cur.is_end = True

    def search(self, word: str) -> bool:
        
        cur = self.root
        for ch in word:
            key = ord(ch) - ord('a')
            if cur.children[key] is None:
                return False
            cur = cur.children[key]
        return cur.is_end
        

    def startsWith(self, prefix: str) -> bool:

        cur = self.root
        for ch in prefix:
            key = ord(ch) - ord('a')
            if cur.children[key] is None:
                return False
            cur = cur.children[key]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)