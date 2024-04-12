# Problem: Turtle vs. Rabbit Race: Optimal Trainings - https://codeforces.com/contest/1933/problem/E

from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import sys

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))

def solve():
    n = int(input())
    nums = intl()
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    ans = []
    for _ in range(int(input())):
        left, u = intl()
        right = bisect_left(prefix, u + prefix[left - 1])
        if right >= len(prefix):
            right -= 1
        elif right > left:
            diff = prefix[right] - prefix[left - 1] - u
            if diff >= 0:
                sum_one = (u*(u + 1)//2) - (abs(diff)*abs(diff - 1)//2)
                rem = u - (prefix[right - 1] - prefix[left - 1])
                sum_two = (u*(u + 1)//2) - (rem*(rem + 1)//2)
                if sum_two >= sum_one:
                    right -= 1
        ans.append(right)
    print(*ans)

t = int(input())
for _ in range(t):
    solve()

