# Problem: They Are Everywhere - https://codeforces.com/problemset/problem/701/C

from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import sys

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))

def solve():
    n = int(input())
    s = input()
    size = len(set(s))
    left = right = 0
    count = defaultdict(int)
    ans = n + 1
    for right in range(n):
        count[s[right]] += 1
        while len(count) == size:
            ans = min(ans, right - left + 1)
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
    print(ans)

#t = int(input())
#for _ in range(t):
solve()

