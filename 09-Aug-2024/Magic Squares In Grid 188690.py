# Problem: Magic Squares In Grid - https://leetcode.com/problems/magic-squares-in-grid/

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        
        n, m = len(grid), len(grid[0])
        ans = 0
        for i in range(n - 2):

            for j in range(m - 2):
                
                sum_set= set()
                nums = set()
                for y in range(j, j + 3):
                    _sum = 0
                    for x in range(i, i + 3):
                        _sum += grid[x][y]
                        nums.add(grid[x][y])
                        if y == j:
                            sum_set.add(sum(grid[x][y : y + 3]))
                    sum_set.add(_sum)
                # diagonal sum
                diagonal_one = 0
                diagonal_two = 0
                for x in range(3):
                    diagonal_one += grid[i + x][j + x]
                    diagonal_two += grid[i + x][j + 2 - x]
                sum_set.add(diagonal_one)
                sum_set.add(diagonal_two)
                if len(sum_set) == 1 and len(nums) == 9 and max(nums) == 9:
                    ans += 1
        return ans





