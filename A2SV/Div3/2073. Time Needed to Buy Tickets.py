class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        mi=0
        idx=0
        while True:
            if tickets[k]==0: break
            if idx==len(tickets): idx=0

            while not tickets[idx]:
                idx+=1
                if idx==len(tickets): idx=0
            tickets[idx]-=1
            idx+=1
            mi+=1
        return mi
        
