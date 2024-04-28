# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import sys

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))

def solve():
    
    def find(x):
        while x != root[x]:
            root[x] = root[root[x]]
            x = root[x]
        return x
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                root[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                root[rootX] = rootY
            else:
                rank[rootX] += 1
                root[rootY] = rootX
    
    n, m, k = intl()
    for _ in range(m):
        input()
    oper = []
    for k in range(k):
        oper.append(input().split())

    root = [i for i in range(n)]
    rank = [0]*n
    ans = []
    for c, a, b in oper[::-1]:
        if c == 'ask':
            if find(int(a) - 1) == find(int(b) - 1):
                ans.append('YES')
            else:
                ans.append('NO')
        else:
            union(int(a) - 1, int(b) - 1)
    for l in ans[::-1]:
        print(l)


#t = int(input())
#for _ in range(t):
solve()

