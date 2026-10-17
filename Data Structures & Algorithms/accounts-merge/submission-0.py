class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        size = {}

        def find(x):
            parent.setdefault(x, x)
            size.setdefault(x, 1)
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        email_to_name = {}
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                email_to_name[email] = name
            for email in acc[2:]:
                union(acc[1], email)

        groups = defaultdict(list)
        for email in email_to_name:
            groups[find(email)].append(email)

        return [[email_to_name[root]] + sorted(emails)
                for root, emails in groups.items()]
