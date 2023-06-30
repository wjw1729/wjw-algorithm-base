mod=10**9+7
f=[1]*(10**4+1)
invf=[1]*(10**4+1)

for i in range(1,10**4+1):
    f[i]=f[i-1]*i
    f[i]%=mod

for i in range(1,10**4+1):
    invf[i]=pow(f[i],mod-2,mod)

def Cni(n,m):
    return f[n]*invf[m]*invf[n-m]%mod



from functools import lru_cache




class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:

        @lru_cache(None)
        def dfs(i, k):
            if k == 0:
                return 1
            else:
                res=0
                for j in range(2*i, maxValue+1,i):
                    res+=dfs(j,k-1)
                    res%=mod

                return res

        f=[[0]*(n) for _ in range(maxValue+1)]

        for i in range(1,maxValue+1):
            for j in range(n-1,-1,-1):
                f[i][j]=dfs(i,j)



        ans=0
        for i in range(1,maxValue+1):

            m=maxValue//i
            for j in range(min(n,m),0,-1):
                ans+=Cni(n-1,j-1)*f[i][j-1]%mod

        return ans%mod

n=5878
maxva=2900

res=Solution().idealArrays(n,maxva)
print(res)