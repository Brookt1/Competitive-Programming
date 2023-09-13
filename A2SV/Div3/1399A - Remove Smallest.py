import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

############ ---- solution ---- ############

n = int(input())
for i in range(n):
    
    l=int(input())
    s=inlt()
    s.sort()
    if l==1:
        print("YES")
        continue
    
    for j in range(l-1):
        if s[j+1] -s[j]>1:
            print('NO')
            break
        if j==l-2: print("YES")
