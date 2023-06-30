class Solution:
    def minTransfers(self, distributions) -> int:
        deg=[0]*12

        for u,v,n in distributions:
            deg[u]-=n
            deg[v]+=n

        f=[0]*(1<<12)

        for i in range(1,1<<12):
            s=0
            for j in range(12):
                if i & (1<<j):
                    s+=deg[j]
            if s==0:
                f[i]=1

        for i in range(1<<12):
            j=i
            while j>0:
                f[i]=max(f[i],f[i-j]+f[j])
                j=(j-1) &i

        return 12-f[(1<<12)-1]








d=[[0,1,5],[1,2,10],[2,0,5],[2,1,1]]
res=Solution().minTransfers(d)
print(res)