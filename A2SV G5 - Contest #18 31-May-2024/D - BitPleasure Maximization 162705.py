# Problem: D - BitPleasure Maximization - https://codeforces.com/gym/526229/problem/D

from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import sys

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None] * 2
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        cur = self.root
        bit_idx = 42
        while bit_idx >= 0:
            bit = 1 if num & (1 << bit_idx) else 0 
            if not cur.children[bit]:
                cur.children[bit] = TrieNode()
            cur = cur.children[bit]
            bit_idx -= 1

    def search(self, num):
        cur = self.root
        bit_idx = 42
        bit_val = 0
        while bit_idx >= 0:
            bit = 1 if num & (1 << bit_idx) else 0
            if bit == 0:
                if cur.children[1]:
                    cur = cur.children[1]
                    bit_val = bit_val | (1 << bit_idx)
                else:
                    cur = cur.children[0]
            else:
                if cur.children[0]:
                    cur = cur.children[0]
                else:
                    cur = cur.children[1]
                    bit_val = bit_val | (1 << bit_idx)
            bit_idx -= 1

        return bit_val ^ num
    
def solve():
    
    n = int(input())
    nums = intl()
    xor = 0
    trie = Trie()
    trie.insert(xor)
    for num in nums:
        xor ^= num
        trie.insert(xor)
    _max = trie.search(0)
    xor = 0
    for num in nums[::-1]:
        xor ^= num
        _max = max(_max, trie.search(xor))
    print(_max)

def main():
# t = int(input())
# for _ in range(t):
    solve()
if __name__ == "__main__":
    main()
    
