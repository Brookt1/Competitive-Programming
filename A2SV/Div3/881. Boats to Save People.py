class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        l,r=0,len(people)-1
        boats=0
        people.sort()
        print(people)
        while l<=r:
            if people[r]>limit: 
                r-=1
            elif people[r]+people[l]>limit:
                r-=1
                boats+=1
            else:
                boats+=1
                r-=1
                l+=1
        return boats
