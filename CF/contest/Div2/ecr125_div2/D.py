import io,os
import bisect
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n,C=[int(x) for x in input().split()]

sls=[0]*(C+1)
for _ in range(n):
    c,x,y=[int(x) for x in input().split()]
    sls[c]=max(sls[c],x*y)


for c in range(1,C+1):
    xy=sls[c]
    if xy==0:
        continue
    for i in range(1,C//c+1):
        sls[i*c]=max(sls[i*c],i*xy)


for i in range(1,C+1):
    sls[i]=max(sls[i],sls[i-1])

m=int(input())
monsters=[]
for _ in range(m):
    x,y = [int(x) for x in input().split()]
    if x*y>=sls[-1]:
        print(-1,end=' ')
    else:
        idx = bisect.bisect_right(sls, x * y)
        print(idx,end=' ')

