

n,m=[int(x) for x in input().split()]
a=[int(x) for  x in input().split()]

b=[0]*n
b2=[0]*n

for i in range(1,n):
    if a[i]<a[i-1]:
        b[i]=-a[i]+a[i-1]

for i in range(1,n):
    if a[i]>a[i-1]:
        b2[i]=a[i]-a[i-1]

presum=[0]*(n+1)
for i in range(1,n+1):
    presum[i]=presum[i-1]+b[i-1]

presum2=[0]*(n+1)

for i in range(1,n+1):
    presum2[i]=presum2[i-1]+b2[i-1]

for _ in range(m):
    s,t=[int(x) for  x in input().split()]
    if t>=s:
        print(presum[t]-presum[s])
    else:
        print(presum2[s]-presum2[t])

