# Problem: C - FunkyLlama's Ribbon Challenge - https://codeforces.com/gym/523525/problem/C

import sys,threading
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))

def solve():
    n, a, b, c = intl()
    memo = {}
    def dp(n):
        if n <= 0:
            if n == 0:
                return 0
            return float('-inf')
        if n not in memo:
            memo[n] = max(dp(n - a) + 1, dp(n - b) + 1, dp(n - c) + 1)
        return memo[n]
    ans = dp(n)
    print(ans)
def main():
# t = int(input())
# for _ in range(t):
    solve()
if __name__ == "__main__":
    threading.Thread(target=main).start()