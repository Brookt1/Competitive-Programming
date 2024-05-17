# Problem: D - Meron and Games - https://codeforces.com/gym/523525/problem/D

from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import collections,sys,threading
sys.setrecursionlimit(10**9)
threading.stack_size(1<<27)

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))

def solve():
    n = int(input())
    nums = intl()
    count = Counter(nums)
    memo = {}
    def dp(n):
        if n < 1:
            return 0

        if n not in memo:
            memo[n] = max(count[n] * n + dp(n - 2), dp(n - 1))
        return memo[n]
    print(dp(max(nums)))


def main():
	#t = int(input())
    #for _ in range(t):
    solve()
if __name__ == "__main__":
    threading.Thread(target=main).start()
