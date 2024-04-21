# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        n = len(recipes)
        graph = defaultdict(list)
        incoming = defaultdict(int)
        supplies = set(supplies)
        rec = set(recipes)
        queue = deque()
        visited = set()
        for i in range(n):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])
                incoming[recipes[i]] += 1
                if ingredient not in rec and ingredient not in visited:
                    queue.append(ingredient)
                    visited.add(ingredient)

        ans = set()
        while queue:
            ingred = queue.popleft()
            if ingred in rec and ingred in ans or ingred in supplies:
                for adj in graph[ingred]:
                    incoming[adj] -= 1
                    if incoming[adj] == 0:
                        ans.add(adj)
                        queue.append(adj)
        return list(ans)

        