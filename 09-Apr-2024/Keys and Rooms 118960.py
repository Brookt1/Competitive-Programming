# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        


        queue = deque([0])
        visited = set()
        visited.add(0)
        while queue:

            for _ in range(len(queue)):
                node = queue.popleft()
                visited.add(node)
                _len = len(queue)
                for adj in rooms[node]:
                    if adj not in visited:
                        queue.append(adj)
        if len(visited) == len(rooms):
            return True
        return False