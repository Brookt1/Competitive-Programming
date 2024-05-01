# Problem: Raising Bacteria - https://codeforces.com/contest/579/problem/A

from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import sys

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))

def solve():
    n = int(input())
    print(n.bit_count())

#t = int(input())
#for _ in range(t):
solve()

