# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        

        five = ten = twenty = 0
        for bill in bills:
            change = bill - 5
            if change == 15:
                if ten > 0:
                    change -= 10
                    ten -= 1
                if 5 * five >= change:
                    five -= change // 5
                else:
                    print(five, change)
                    return False
                twenty += 1
            elif change == 5:
                if five > 0:
                    five -= 1
                else:
                    return False
                ten += 1
            else:
                five += 1
        return True
