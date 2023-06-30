mod = 10 ** 9 + 7
f=[0]*(10**5+1)

f[0]=1
for i in range(1,10**5+1):
    f[i]=f[i-1]*i
    f[i]%=mod

invf=[1]*(10**5+1)
for i in range(1,10**5+1):
    invf[i]=pow(f[i],mod-2,mod)

def cni(n,i):
    return f[n]*invf[i]*invf[n-i]%mod

t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    if n==1:
        print(1)

    elif (a[0]==0 and a[-1]==1) or (a[0]==1 and a[-1]==0):
        print(f[n-2])
    elif a[0]==0 or a[0]==1:
        idx=a.index(1-a[0])

        pre=a[-1]
        c0=0
        for i in range(n-1,idx,-1):
            if a[i]<pre:
                c0+=1
                pre=a[i]

        c1=a[-1]-2-c0

        ans=cni(idx-1,a[-1]-2-c0)*f[a[-1]-2-c0]*f[n-3-c0-c1]%mod
        print(ans)

    elif a[-1]==0 or a[-1]==1:
        idx=a.index(1-a[-1])

        pre=a[0]
        c0=0
        for i in range(0,idx):
            if a[i]<pre:
                c0+=1
                pre=a[i]

        c1=a[0]-2-c0
        ans=cni(n-1-idx-1,c1)*f[c1]*f[n-3-c0-c1]%mod
        print(ans)
    else:
        idx1=a.index(0)
        idx2=a.index(1)

        if idx1>idx2:
            idx1,idx2=idx2,idx1


        c0
        pre=a[0]
        for i in range(idx1):
            if a[i]<pre:
                c0+=1
                pre=a[i]

        pre=a[-1]
        c1=0
        for j in range(n-1,idx2,-1):
            if a[i]<pre:
                c1+=1
                pre=a[i]

        a0,an=a[0],a[n-1]
        if a0>an:
            a0,an=an,a0

        print(-1)






