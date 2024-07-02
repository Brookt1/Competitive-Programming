# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort()
        nums2.sort()
        first = second = 0
        ans = []
        while first < len(nums1) and second < len(nums2):
            if nums1[first] > nums2[second]:
                second += 1
            elif nums1[first] < nums2[second]:
                first += 1
            else:
                ans.append(nums1[first])
                first += 1
                second += 1
        return ans