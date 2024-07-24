# Problem: B - Mohammed's Magical Cleaning Machine - https://codeforces.com/gym/537362/problem/B

from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import sys

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))

def solve():
    
    n = int(input())
    nums = intl()
    non_zero = 0
    zero = 0
    for num in nums[:n - 1]:
        if num:
            non_zero += num
        if non_zero and num == 0:
            zero += 1
    if non_zero:
        print(non_zero + zero)
    else:
        print(zero)

        


def main():
    t = int(input())
    for _ in range(t):
        solve()
if __name__ == "__main__":
    main()
    # sys.setrecursionlimit(10 **8 )
    # threading.stack_size(2 * 10 ** 8)
    
    # main_thread = threading.Thread(target=main)
    # main_thread.start()
    # main_thread.join()
