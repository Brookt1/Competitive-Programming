# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import sys

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))

def solve():
    
    n = int(input())
    if n.bit_count() > 1:
        one = 1
        while n & one == 0:
            one <<= 1
        print(one)
    else:
        if n == 1 or n == 2:
            print(3)
        else:
            print(n + 1)

t = int(input())
for _ in range(t):
    solve()

