# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D


import sys
def intl():
    return list(map(int,sys.stdin.readline().split()))
 
 
for _ in range(int(input())):
    n = input()
    nums = intl()
    count = [0]
    def merge_sort(left, right):
        if left == right:
            return [nums[left]]
        mid = left + (right - left)//2
        left_half = merge_sort(left, mid)
        right_half = merge_sort(mid + 1, right)
        if left_half[0] > right_half[-1]:
            count[0] += 1
            return right_half + left_half
        return left_half + right_half
 
    sorted_arr = merge_sort(0 , len(nums) - 1)
    for i in range(len(nums) - 1):
        if sorted_arr[i] >= sorted_arr[i + 1]:
            count[0] = -1
            break
    print(count[0])
