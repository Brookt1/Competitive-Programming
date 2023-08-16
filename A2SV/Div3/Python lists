if __name__ == '__main__':
    N = int(input())
    L=[]
    for i in range(N):
        s=input().split()
        lenS=len(s)
        if lenS==1:
            if s[0]=='sort':
                L.sort()
            elif s[0]=='pop':
                L.pop()
            elif s[0]=='print':
                print(L)
            else:
                L.reverse()
        else:
            if s[0]=='insert':
                L.insert(int(s[1]),int(s[2]))
            elif s[0]=='remove':
                L.remove(int(s[1]))
            else:
                L.append(int(s[1]))
