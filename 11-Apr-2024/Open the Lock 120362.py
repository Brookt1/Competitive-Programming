# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        graph = defaultdict(list)
        for i in range(10000):
            num = (4 - len(str(i)))*'0' + str(i)
            for i in range(4):
                new = ''
                if num[i] == '9':
                    new = num[:i] + '0' + num[i + 1:]
                else:
                    new = num[:i] + str(int(num[i]) + 1) + num[i + 1: ]
                graph[num].append(new)
                graph[new].append(num)

        queue = deque([['0000', 0]])
        visited = set()
        visited.add('0000')
        while queue:
            for _ in range(len(queue)):
                node, depth = queue.popleft()
                if node == target:
                    return depth
                for adj in graph[node]:
                    if  adj not in visited and adj not in deadends:
                        visited.add(adj)
                        queue.append([adj, depth + 1])
        return -1