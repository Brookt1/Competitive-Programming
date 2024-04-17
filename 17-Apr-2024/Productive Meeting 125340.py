# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import sys
from heapq import *

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))

def solve():
    count = 0
    max_heap = []
    def push(num, idx):
        if num > 0:
            heappush(max_heap, [-1*num, idx])
    
    n = int(input())
    nums = intl()
    ans = []
    for i in range(n):
        push(nums[i], i)
    while len(max_heap) > 1:
        max, max_idx = heappop(max_heap)
        min, min_idx = heappop(max_heap)
        ans.append([min_idx, max_idx])
        push(abs(max) - 1, max_idx)
        push(abs(min) - 1, min_idx)
    print(len(ans))
    for l, r in ans:
        print(l+1, r+1)

t = int(input())
for _ in range(t):
    solve()

