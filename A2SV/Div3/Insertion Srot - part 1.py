
def insertionSort1(n, arr):
    key=arr[-1]
    for i in range(n-1,-1,-1):
        if(key<arr[i-1]):
            arr[i]=arr[i-1]

        else:
            arr[i]=key
            s=' '.join(map(str,arr))
            print(s)
            break
        s=' '.join(map(str,arr))
        print(s)
        
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
