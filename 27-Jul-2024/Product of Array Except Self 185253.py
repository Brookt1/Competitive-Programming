# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre_pro = [1]
        suf_pro = [1]
        for i in range(len(nums)):
            pre_pro.append(pre_pro[-1]*nums[i])
            suf_pro.append(suf_pro[-1]*nums[len(nums) - i - 1])
        suf_pro.reverse()
        res = []
        for i in range(1,len(pre_pro)):
            res.append(pre_pro[i-1]*suf_pro[i])
        return res

        