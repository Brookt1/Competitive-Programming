# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode():
    def __init__(self):
        self.is_end = False
        self.children =  [None for _ in range(26)]
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            key = ord(ch) - ord('a')
            if not cur.children[key]:
                cur.children[key] = TrieNode()
            cur = cur.children[key]
        cur.is_end = True
    

    def search(self, word: str) -> bool:

        def recu(node, idx):
            if not node:
                return False
                
            if idx + 1 == len(word):
                if word[idx] == '.':
                    for child in node.children:
                        if not child is None and child.is_end:
                            return True
                    return False
                child = node.children[ord(word[idx]) - ord('a')]

                return not child is None  and child.is_end
            
            ans = False
            if word[idx] == '.':
                for child in node.children:
                    if not child is None:
                        ans = ans or recu(child, idx + 1)
            else:
                ans = ans or recu(node.children[ord(word[idx])  - ord('a')], idx + 1)
            return ans
        return recu(self.root, 0)
                

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)