# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        arr = []
        for idx, num in enumerate(nums):
            temp = []
            for ch in str(num):
                temp.append(mapping[int(ch)])
            arr.append([int(''.join( str(x) for x in temp)), idx, num])
        arr.sort()
        return [num for _, __ , num in arr]