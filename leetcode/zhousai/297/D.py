from collections import defaultdict

class DisJoinUnion:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[1]*n

    def find(self,x):
        if self.parent[x]==x:
            return x
        return self.find(self.parent[x])

    def union(self,x,y):
        fx,fy=self.find(x),self.find(y)

        if fx==fy:
            return

        if self.rank[fx]<self.rank[fy]:
            fx,fy=fy,fx

        self.parent[fy]=fx
        self.rank[fx]+=self.rank[fy]




class Solution:
    def distinctNames(self, ideas) -> int:

        d=defaultdict(int)
        for s  in ideas:
            d[s[1:]]|=1<<(ord(s[0])-ord('a'))


        cnt=[[0]*26 for _ in range(26)]

        for mask in d.values():
            for i in range(26):
                if mask & (1<<i)==0:
                    for j in range(26):
                        if mask & (1<<j):
                            cnt[i][j]+=1

        ans=0
        for mask in  d.values():
            for i in range(26):
                if mask &(1<<i):
                    for j in range(26):
                        if mask & (1<<j)==0:
                            ans+=cnt[i][j]

        return  ans




