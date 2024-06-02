# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        n = len(arr)
        ans = [''] * n
        for word in arr:
            ans[int(word[-1]) - 1] = word[:len(word) - 1]
        return ' '.join(ans)