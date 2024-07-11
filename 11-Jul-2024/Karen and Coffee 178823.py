# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

import sys
def intl():
    return list(map(int,sys.stdin.readline().split()))

n=200000
query=[0]*(n+1)
l,k,q=intl()

for i in range(l):
    left,right=intl()
    query[left]+=1
    if right<n:
        query[right+1]-=1

prefix=[0]*(n+1)
for i in range(1,n+1):
    query[i]+=query[i-1]
    if query[i]>=k:
        prefix[i]+=1
    prefix[i]+=prefix[i-1]
for i in range(q):
    a,b=intl()
    print(prefix[b]-prefix[a-1])