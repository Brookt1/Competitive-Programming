# Problem: F -  A Permutation Puzzle - https://codeforces.com/gym/515998/problem/F

from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import sys, math

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))

def solve():
    n = int(input())
    s = input()
    perm = intl()

    cycle = []
    for i in range(0, n):
        if perm[i]:
            idx = i
            val = []
            while perm[idx]:
                val.append(idx)
                idx = perm[val[-1]] - 1
                perm[val[-1]] = 0
            cycle.append(val)
    ans = 1
    for i in range(len(cycle)):
        orginal = [s[j] for j in cycle[i]]
        count = 0
        for j in range(len(orginal)):
            count += 1
            new_letter  = orginal[j + 1: ] + orginal[: j + 1]
            if new_letter == orginal:
                break

        ans = math.lcm(ans, count)
    print(ans)

t = int(input())
for _ in range(t):
    solve()

