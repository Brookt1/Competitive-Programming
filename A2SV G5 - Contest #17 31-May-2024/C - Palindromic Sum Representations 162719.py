# Problem: C - Palindromic Sum Representations - https://codeforces.com/gym/524965/problem/C



import sys

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))




def solve():

    max_len = int(1e4) * 4  + 1
    mod = int(1e9) + 7

    nums = [0] * ( max_len)
    nums[0] = 1
    coins = []
    for i in range(1, max_len):
        if str(i)  == str(i)[::-1]:
            coins.append(i)

    for coin in coins:
        for i in range(coin, max_len):
            nums[i] = (nums[i] + nums[i - coin])%mod
            

    for _ in range(int(input())):
        n = int(input())
        print((nums[n]))
 
solve()

