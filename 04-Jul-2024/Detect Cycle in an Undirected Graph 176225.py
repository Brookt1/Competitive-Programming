# Problem: Detect Cycle in an Undirected Graph - https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:

		indegree = []
		visited = set()
		queue = deque()
		for i, neighbour in enumerate(adj):
		    indegree.append(len(neighbour))
		    if len(neighbour) < 2:
		        queue.append(i)
		        visited.add(i)
    	while queue:
    	    for _ in range(len(queue)):
		        node = queue.popleft()
		         
		        for neighbour in adj[node]:
		            indegree[neighbour] -= 1
		            if indegree[neighbour] == 1 and neighbour not in visited:
		                visited.add(neighbour)
		                queue.append(neighbour)
		
		return len(visited) != V