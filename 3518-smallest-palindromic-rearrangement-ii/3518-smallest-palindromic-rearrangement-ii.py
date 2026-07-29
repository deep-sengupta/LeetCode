from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        c=Counter(s)
        h={x:y//2 for x,y in c.items()}
        m=next((x for x,y in c.items() if y&1),"")
        a=sorted(h)
        n=sum(h.values())

        def f(t):
            r=l=1
            l=t
            for x in a:
                if h[x]:
                    r*=comb(l,h[x])
                    if r>=k:return k
                    l-=h[x]
            return r

        if f(n)<k:return ""
        p=[]
        while n:
            for x in a:
                if not h[x]:continue
                h[x]-=1
                w=f(n-1)
                if w>=k:
                    p.append(x)
                    n-=1
                    break
                k-=w
                h[x]+=1
        p="".join(p)
        return p+m+p[::-1]