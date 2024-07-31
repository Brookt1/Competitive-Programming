# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        res=0
        dic=defaultdict(int)
        for right in range(len(fruits)):
            dic[fruits[right]]+=1
            while len(dic)>2:
                dic[fruits[left]]-=1
                if dic[fruits[left]]<1:
                    del dic[fruits[left]]
                left+=1
            res=max(res,right-left+1)
        return res


        