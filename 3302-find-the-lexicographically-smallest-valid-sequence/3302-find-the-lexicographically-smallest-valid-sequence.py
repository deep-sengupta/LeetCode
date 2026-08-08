class Solution:
    def validSequence(self, a: str, b: str) -> list[int]:
        r=[-1]*len(b);j=len(b)-1
        for i in range(len(a)-1,-1,-1):
            if j>=0 and a[i]==b[j]:r[j]=i;j-=1
        ans=[];j=x=0
        for i,c in enumerate(a):
            if j<len(b) and (c==b[j] or (not x and (j+1==len(b) or i<r[j+1]))):
                ans.append(i);x|=c!=b[j];j+=1
        return ans if j==len(b) else []
