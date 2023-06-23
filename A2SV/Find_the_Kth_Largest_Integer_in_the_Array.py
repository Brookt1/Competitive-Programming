#leetcode problem
#1985. Find the Kth Largest Integer in the Array


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=lambda x:int(x),reverse=True)
        return str(nums[k-1])