
mod=10**9+7
f=[1]*(4*10**5+1)
invf=[1]*(4*10**5+1)

for i in range(1,4*10**5+1):
    f[i]=f[i-1]*i
    f[i]%=mod
    invf[i]=pow(f[i],mod-2,mod)




def cni(a,b):
    if a<b:
        return 0
    return (f[a]*invf[b]*invf[a-b])%mod


n=int(input())
a=[int(x) for x in input().split()]

ans=0
for i in range(n+1):
    ans+=cni(i+a[i],i+1)
    ans%=mod




print(ans)

