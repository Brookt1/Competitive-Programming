# Problem: A - Flag Checker - https://codeforces.com/gym/515998/problem/A

from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import sys

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))

def solve():
    n, m = intl()
    colors = []
    flag = True
    for _ in range(n):
        line = input()
        num = list(set(line))
        if len(line) != m or len(num) != 1 or colors and num[0] == colors[-1]:
            flag = False
            break
        else:
            colors.append(num[0])
    if flag:
        print('YES')
    else:
        print('NO')
            


solve()

