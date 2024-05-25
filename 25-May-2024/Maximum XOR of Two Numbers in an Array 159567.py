# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [-1, -1]

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        cur = self.root
        bit_idx = 30
        while bit_idx >= 0:
            bit = 1 if num & (1 << bit_idx) else 0 
            if cur.children[bit] == -1:
                cur.children[bit] = TrieNode()
            cur = cur.children[bit]
            bit_idx -= 1

    def search(self, num):
        cur = self.root
        bit_idx = 30
        bit_val = []
        while bit_idx >= 0:
            bit = 1 if num & (1 << bit_idx) else 0
            if bit == 0:
                if cur.children[1] != -1:
                    cur = cur.children[1]
                    bit_val.append(1)
                else:
                    cur = cur.children[0]
                    bit_val.append(0)
            else:
                if cur.children[0] != -1:
                    cur = cur.children[0]
                    bit_val.append(0)
                else:
                    cur = cur.children[1]
                    bit_val.append(1)
            bit_idx -= 1

        return int(''.join(str(x) for x in bit_val), 2)
    
        


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        trie = Trie()
        for num in nums:
            trie.insert(num)
        ans = 0
        for num in nums:
            ans = max(ans, trie.search(num) ^ num)
        return ans
        

