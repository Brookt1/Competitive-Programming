# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import sys, math

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))


def solve():
    n = int(input())
    nums = intl()
    count = defaultdict(int)
    for x in nums:
        num = x
        while num % 2 == 0:
            num //= 2
            count[2] += 1
        
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            while num % i == 0:
                num //= i
                count[i] += 1
        if num > 1:
            count[num] += 1
    flag = False
    for val in count.values():
        if val % n != 0:
            flag = True
            break
    if flag:
        print('NO')
    else:
        print('YES')
    
t = int(input())
for _ in range(t):
    solve()
