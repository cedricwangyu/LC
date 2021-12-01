class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent={}
        group=defaultdict(list)
        result=[]
        emailToName={}

        def find(x):
            if x==parent[x]:
                return x
            parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            r1=find(x)
            r2=find(y)
            if r1!=r2:
                parent[r2]=r1

        for account in accounts:
            emailToName[account[1]]=account[0]
            for email in account[1:]:
                parent[email]=email           

        for account in accounts:
            email1=account[1]
            for email2 in account[2:]:
                union(email1,email2)

        for email in parent:
            group[find(email)].append(email)

        for key in group:
            result.append([emailToName[key]]+sorted(group[key]))

        return result
