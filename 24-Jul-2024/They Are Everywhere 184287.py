# Problem: They Are Everywhere - https://codeforces.com/problemset/problem/701/C

from collections import defaultdict

n = int(input())
s = input()
size = len(set(s))
left = 0
dic = defaultdict(int)
ans = float('inf')
for right in range(n):
    dic[s[right]] += 1
    while len(dic) == size:
        ans = min(ans, right - left + 1)
        dic[s[left]] -= 1
        if dic[s[left]] == 0:
            del dic[s[left]]
        left += 1
print(ans)
    
