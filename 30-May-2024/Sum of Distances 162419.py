# Problem: Sum of Distances - https://leetcode.com/problems/sum-of-distances/

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        

        n = len(nums)
        dic = {}
        for i in range(n):
            num = nums[i]
            if num not in dic:
                dic[num] = [[0, i], 1]
            else:
                dic[num][0].append(dic[num][0][-1] + i)
        
        arr = []
        for i in range(n):
            num = nums[i]
            prefix = dic[num][0]
            idx = dic[num][1]
            valid_idx = prefix[idx] - prefix[idx - 1]
            left = (valid_idx) * idx - prefix[idx]
            right = (prefix[-1] - prefix[idx - 1]) - valid_idx * (len(prefix) - idx)
            dic[num][1] += 1
            arr.append(left + right)

        return arr

                