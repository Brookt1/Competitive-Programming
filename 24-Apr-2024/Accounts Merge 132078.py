# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        

        root = { }
        name = {}
        rank = defaultdict(int)


        def find(email):
            while email != root[email]:
                root[email] = root[root[email]]
                email = root[email]
            return email
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
        emails = []
        for acc in accounts:
            person = acc[0]
            val =  [ ]
            for email in acc[1:]:
                val.append(email)
                root[email] = email
                name[email] = person
            emails.append(val)
        for email in emails:
            for i in range(len(email) - 1):
                union(email[i], email[i + 1])

        data = defaultdict(list)
        for key, val in root.items():
            rootVal = find(val)
            data[rootVal].append(key)
        ans = []
        for key, val in data.items():
            ans.append([name[key]] + sorted(val))
        return ans
 

        
