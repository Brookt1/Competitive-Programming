#leetcode problem
#179. Largest Number
# medium

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=list(map(str,nums))

        def compare(n1,n2):
            if n1+n2>n2+n1:
                return -1
            else:
                return 1
        num=sorted(nums,key=cmp_to_key(compare))
        return str(int("".join(num)))