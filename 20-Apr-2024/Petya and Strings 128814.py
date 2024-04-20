# Problem: Petya and Strings - https://codeforces.com/problemset/problem/112/A

from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import sys

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))

def solve():
    s1 = input().lower()
    s2 = input().lower()
    if s1 == s2:
        print(0)
    elif s1 > s2:
        print(1)
    else:
        print(-1)


#t = int(input())
#for _ in range(t):
solve()

