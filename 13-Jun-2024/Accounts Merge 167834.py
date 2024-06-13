# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        

        def find(a):
            while root[a] != root[root[a]]:
                root[a] = root[root[a]]
                a = root[a]
            return root[a]
        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            if rootA != rootB:
                if rank[rootA] > rank[rootB]:
                    root[rootB] = rootA
                elif rank[rootA] < rank[rootB]:
                    root[rootA] = rootB
                else:
                    root[rootB] = rootA
                    rank[rootA] += 1
        

        rank = defaultdict(int)
        root = {}
        dic = {}
        emails = set()
        for account in accounts:
            for address in account[1:]:
                root[address] = address
                dic[address] = account[0]
                emails.add(address)
        for account in accounts:
            for i in range(2, len(account)):
                union(account[i - 1], account[i])
        union_dic = defaultdict(list)

        for email in emails:
            union_dic[find(email)].append(email)
        ans = []

        for key, val in union_dic.items():
            ans.append([dic[key]] + sorted(val)[:])
        return ans
        
