# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import sys

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))

def solve():
    n, k = intl()
    if 9 * n < k or k == 0 and n > 1:
        print(-1, -1)
        return
    _max = []
    s = k
    for i in range(n):
        if s > 9:
            s -= 9
            _max.append(str(9))
        else:
            _max.append(str(s))
            s = 0
    s = k
    _min = [0] * n
    _min[0] = 1
    s -= 1
    for i in range(n):
        if s > 9:
            s -= 9
            _min[(n - i )- 1] = 9
        else:
            _min[(n - i)  - 1] += s
            s = 0

    print(''.join(str(x) for x in _min), ''.join(_max))

#t = int(input())
#for _ in range(t):
solve()

