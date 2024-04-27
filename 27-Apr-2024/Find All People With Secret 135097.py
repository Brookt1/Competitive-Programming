# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        

        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x
        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA != rootB:
                if rank[rootA] > rank[rootB]:
                    root[rootB]  = rootA
                elif rank[rootA] < rank[rootB]:
                    root[rootA] = rootB
                else:
                    root[rootB] = rootA
                    rank[rootA] += 1
        
        root = [i for i in range(n)]
        rank = [0]*n
        rank[0] = float('inf')
        meetings.sort(key = lambda x : x[2])
        union(0, firstPerson)

        flag = last = False
        left = right = 0
        while right < len(meetings):
            while flag and left < right or last and left <= right:
                a, b = meetings[left][:2]

                if find(a) != 0:
                    root[a] = a
                    root[b] = b
                left += 1
            if not last:
                a, b, t = meetings[right]
                if meetings[left][2] != t:
                    flag = True
                else:
                    flag = False
                    union(a, b)
                    if right + 1 == len(meetings) and not last:
                        last = True
                        continue
                    right += 1
            else:
                break
        ans = []
        for i in range(n):
            if find(i) == 0:
                ans.append(i)
        return ans

