# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        memo = {}
        def dp(idx, paid_day):
            if idx == len(days):
                return 0
            state = (idx, paid_day)

            if state not in memo:
                if paid_day <= days[idx]:
                    memo[state] = min(costs[0] + dp(idx + 1, days[idx] + 1), costs[1] + dp(idx + 1, days[idx] + 7), costs[2] + dp(idx + 1, days[idx] + 30))
                else:
                    memo[state] = dp(idx + 1, paid_day)
            return memo[state]
        return dp(0, days[0])

