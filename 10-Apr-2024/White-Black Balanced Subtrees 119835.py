# Problem: White-Black Balanced Subtrees - https://codeforces.com/contest/1676/problem/G

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
    s = input()
    graph = defaultdict(list)

    for i in range(2, n + 1):
        graph[i].append(nums[i - 2])
        graph[nums[i - 2]].append(i)
    visited = set()
    ans = 0
    def dfs(node):
        nonlocal ans

        visited.add(node)
        b, w = 0, 0
        if graph[node]:
            for adj in graph[node]:
                if adj not in visited:
                    x, y =  dfs(adj)
                    w += x
                    b += y
        if s[node - 1] == 'W':
            w += 1
        else:
            b += 1
        if w == b:
            ans += 1

        return [w, b]
    dfs(1)
    print(ans)
def main():
    t = int(input())
    for _ in range(t):
        solve()
if __name__ == "__main__":
    threading.Thread(target=main).start()