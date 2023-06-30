
p=input()
mod=10**9+7

n=len(p)
f=[0]*(n+1)

pre=0
lasta=-1
tt=0
bt=0

for i in range(1,n+1):
    if p[i-1]=='a':
        f[i]=bt+1
        f[i]%=mod
        tt+=f[i]

    if p[i-1]=='b':
        pre=i
        bt=tt


print(sum(f)%mod)



