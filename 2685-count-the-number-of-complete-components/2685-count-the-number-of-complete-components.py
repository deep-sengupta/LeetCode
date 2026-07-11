class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g=[[]for _ in range(n)]
        for a,b in edges:
            g[a]+=b,
            g[b]+=a,
        vis=[0]*n
        ans=0
        for i in range(n):
            if vis[i]:continue
            s=[i];vis[i]=1;c=[]
            while s:
                x=s.pop();c.append(x)
                for y in g[x]:
                    if not vis[y]:
                        vis[y]=1
                        s.append(y)
            ans+=sum(map(lambda x:len(g[x]),c))==len(c)*(len(c)-1)
        return ans