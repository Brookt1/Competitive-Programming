# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        

        n = len(words)
        val = []
        for i in range(n):
            cur = 0
            word = list(set(words[i]))
            for j in range(len(word)):
                cur ^= 1 << (ord(word[j]) - ord('a') + 1)
            val.append(cur)

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                val1 = val[i]
                val2 = val[j]
                while (val1 and val2 ) and (val1 & 1 != 1 or val2 & 1 != 1):
                    val1 >>= 1
                    val2 >>= 1
                if (val1 & 1 != 1 or val2 & 1 != 1):
                    ans = max(len(words[i])*len(words[j]), ans)
        return ans

