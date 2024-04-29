# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

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
    def union(a, b):
        rootA = find(a)
        rootB = find(b)
        if rootA != rootB:
            if size[rootA] > size[rootB]:
                _min, _max = data[rootB - 1]
                data[rootA - 1] = [min(data[rootA - 1][0], _min), max(data[rootA - 1][1], _max)]
                size[rootA] += size[rootB]
                root[rootB] = rootA 
            else: 
                _min, _max = data[rootA - 1]
                data[rootB - 1] = [min(data[rootB - 1][0], _min), max(data[rootB - 1][1], _max)]
                size[rootB] += size[rootA]
                root[rootA] = rootB


    
    n, m = intl()
    root = {i:i for i in range(1, n + 1)}
    size = {i:1 for i in range(1, n + 1)}
    data = [[i, i] for i in range(1, n + 1)]
    ans = [ ]
    for _ in range(m):
        line = input().split()
        if len(line) > 2:
            union(int(line[1]), int(line[2]))
        else:
            ans.append(data[find(int(line[1])) - 1] + [size[find(int(line[1]))]])
    for l in ans:
        print(*l)
    


#t = int(input())
#for _ in range(t):
solve()

