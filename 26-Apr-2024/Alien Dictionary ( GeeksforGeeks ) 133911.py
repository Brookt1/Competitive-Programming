# Problem: Alien Dictionary ( GeeksforGeeks ) - https://www.geeksforgeeks.org/problems/alien-dictionary/1



from collections import defaultdict, deque
class Solution:
    def findOrder(self,alien_dict, N, K):
        
        
        
        indegree = [0]*K
        graph = defaultdict(list)
        for i in range(1, N):
            m = min(len(alien_dict[i]), len(alien_dict[i - 1]))
            idx = 0
            while idx < m and alien_dict[i][idx] == alien_dict[i - 1][idx]:
                idx += 1
            if idx < m :
                graph[alien_dict[i - 1][idx]].append(alien_dict[i][idx])
                indegree[ord(alien_dict[i][idx]) - ord('a')] += 1
        queue = deque()
        for i  in range(k):
            if indegree[i] == 0:
                queue.append(chr(i + ord('a')))
        
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)
            for adj in graph[node]:
                ch = ord(adj) - ord('a')
                indegree[ch] -= 1
                if indegree[ch] == 0:
                    queue.append(adj)
        return ''.join(ans)
    
