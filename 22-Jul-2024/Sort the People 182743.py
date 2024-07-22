# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        

        arr = list(zip(heights, names))
        arr.sort(reverse = True)

        return [name for height, name in arr]