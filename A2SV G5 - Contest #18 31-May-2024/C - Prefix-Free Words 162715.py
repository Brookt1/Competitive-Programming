# Problem: C - Prefix-Free Words - https://codeforces.com/gym/526229/problem/C

import sys

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None, None]
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ans = []
    
    def insert(self, n, node):
        stack = []
        word = []
        for i in range(n):
            stack.append(node)
            if node.children[0] is None or not node.children[0].is_end:
                if node.children[0] is None:
                    node.children[0]  = TrieNode()
                node = node.children[0]
                word.append('0')
            elif node.children[1] is None or not node.children[1].is_end:
                if node.children[1] is None:
                    node.children[1] = TrieNode()
                node = node.children[1]
                word.append('1')
            else:
                return False
        node.is_end = True 

        while stack and stack[-1].children[1] and stack[-1].children[0]:
            prev = stack.pop()
            prev.is_end = True
        return ''.join(word)

    

def solve():
    n = int(input())
    nums = sorted(zip(map(int, input().split()), range(n)))
    trie = Trie()
    ans = [''] * n
    for num, idx in nums:
        res = trie.insert(num, trie.root)
        if res == False:
            print('NO')
            return
        ans[idx] = res
        
    print('YES')
    for l in ans:
        print(l)
    
def main():
	#t = int(input())
    #for _ in range(t):
    solve()
if __name__ == "__main__":
    main()