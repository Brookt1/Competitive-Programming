# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import sys
from heapq import *

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))

def solve():
    n = int(input())
    heap = []
    ans = []
    for i in range(n):
        line = input().split()
        if len(line) < 2 and line[0] == 'removeMin':
            if not heap:
                ans.append('insert 0')
            else:
                heappop(heap)
            ans.append(line[0])
        elif line[0] == 'insert':
            heappush(heap, int(line[1]))
            ans.append(line[0] + ' ' + line[1])
        elif line[0] == 'getMin':
            if not heap or  heap[0] > int(line[1]):
                ans.append('insert' + ' ' + line[1])
                heappush(heap, int(line[1]))
            elif heap[0] < int(line[1]):
                while heap and heap[0] < int(line[1]):
                    ans.append('removeMin')
                    heappop(heap)
                if not heap or heap[0] > int(line[1]):
                    ans.append('insert ' + line[1])
                    heappush(heap, int(line[1]))
            ans.append(line[0] + ' ' + line[1])
    print(len(ans))
    for l in ans:
        print(l)
                







#t = int(input())
#for _ in range(t):
solve()

