# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
import sys

input = lambda: sys.stdin.readline().strip()
intl = lambda: list(map(int, input().split()))

def solve():
    
    n = int(input())
    word = input()
    graph = defaultdict(list)
    incoming = defaultdict(int)
    for _ in range(n - 1):
        line = input()
        left, right = 0, 0
        while left < len(word) and right < len(line):
            if word[left] != line[right]:
                graph[word[left]].append(line[right])
                incoming[line[right]] += 1
                break
            left += 1
            right += 1
            if (left == len(word) or right == len(line)) and len(line) < len(word):
                print('Impossible')
                exit()
        word = line
    queue = deque()
    ans = []
    for i in range(26):
        if incoming[chr(ord('a') + i)] == 0:
            queue.append(chr(ord('a') + i))
    while queue:
        node = queue.popleft()
        ans.append(node)
        for adj in graph[node]:
            incoming[adj] -= 1
            if incoming[adj] == 0:
                queue.append(adj)
    if len(ans) != 26:
        print('Impossible')
    else:
        print(''.join(ans))
    
#t = int(input())
#for _ in range(t):
solve()

