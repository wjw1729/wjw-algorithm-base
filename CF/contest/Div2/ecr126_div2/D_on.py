import math

n,k=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]

ans=0
tt=0
cnt=0
closed=[0]*n
for i in range(n-1,-1,-1):
    tt-=cnt
    cnt-=closed[i]
    b[i]-=tt
    if b[i]<=0:
        continue

    el=min(i+1,k)
    need=math.ceil(b[i]/el)
    tt+=need*el
    cnt+=need
    ans+=need
    if i-el>=0:
        closed[i-el]+=need

print(ans)


