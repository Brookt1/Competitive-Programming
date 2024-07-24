# Problem: A - Se7en - https://codeforces.com/gym/537362/problem/A

from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import sys

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))

def solve():
    n = int(input())
    if n % 7 == 0:
        print(n)
    else:
        n = int(str(n)[:len(str(n)) - 1] + '0')
        while n % 7 != 0:
            n += 1
        print(n)
        

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
