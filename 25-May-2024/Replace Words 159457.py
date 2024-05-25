# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end = True
    def search(self, word):

        queue = deque([[self.root, 0]])
        while queue:
            node, idx = queue.popleft()

            
            if node.is_end:
                return word[:idx]
            if idx == len(word) or word[idx] not in node.children:
                return word
            queue.append([node.children[word[idx]], idx + 1])



class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        ans = []
        for word in sentence.split():

            res = trie.search(word)
            ans.append(res)
        return ' '.join(ans)
