# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import sys

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))

def solve():
    
    n, m, k = intl()
    nums = []
    for _ in range(m + 1):
        nums.append(int(input()))
    last = nums[-1]
    ans = 0
    for num in nums[:m]:
        temp = last
        count = 0
        while temp or num:
            if (temp & 1) != (num & 1):
                count += 1
            temp >>= 1
            num >>= 1
        if count <= k:
            ans += 1
    print(ans)

#t = int(input())
#for _ in range(t):
solve()

