# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:

        dic = Counter(word)
        arr = [[val, key] for key, val in dic.items()]
        arr.sort(reverse = True)
        print(arr)
        ans = 0
        for i in range(1, len(arr) + 1):
            ans += ceil(i / 8) * arr[i - 1][0]
        return ans

