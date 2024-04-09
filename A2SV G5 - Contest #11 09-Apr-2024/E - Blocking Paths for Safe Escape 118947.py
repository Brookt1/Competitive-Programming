# Problem: E - Blocking Paths for Safe Escape - https://codeforces.com/gym/515998/problem/E

from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import sys

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))
dir = [[0,1], [0, -1], [-1, 0], [1, 0]]
def solve():
    m, n = intl()
    def inbound(row, col):
        return (0 <= row < m) and (0 <= col < n)

    grid = []
    for _ in range(m):
        line = input()
        grid.append([ch for ch in line])
    flag = ''
    good = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'B':
                for x, y in dir:
                    _row = i + x
                    _col = j + y
                    if inbound(_row, _col):
                        if grid[_row][_col] == 'G':
                            flag = True
                        elif grid[_row][_col] == '.':
                            grid[_row][_col] = '#'
            elif grid[i][j] == 'G':
                good.add((i, j))
    stack = []
    if not flag and grid[m - 1][n - 1] not in ('#', 'B'):
        stack = [[m - 1, n - 1]]
    visited = set()
    
    while stack:
        row, col = stack.pop()
        visited.add((row, col))
        if (row, col) in good:
            good.remove((row, col))
        for x, y in dir:
            _row = row + x
            _col = col + y
            if inbound(_row, _col) and (_row, _col) not in visited and grid[_row][col] != 'B' and grid[_row][_col] != '#':
                stack.append([_row, _col])

    if len(good) or flag:
        print('No')
    else:
        print('Yes')



        




t = int(input())
for _ in range(t):
    solve()

