from collections import deque

def nearestpoints(pls):



    indexmap={(x,y):i   for i,(x,y) in enumerate(pls)}
    ans=[None]*n
    q = deque()

    for i in range(n):
        x,y=pls[i]
        for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if (nx,ny) in indexmap:
                continue
            ans[i]=(nx,ny)
            q.append((x,y))
            break

    while q:
        x,y=q.popleft()

        for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if (nx,ny) in indexmap:
                j=indexmap[(nx,ny)]
                if ans[j]!=None:
                    continue
                ans[j]=ans[indexmap[(x,y)]]
                q.append((nx,ny))

    return ans











n=int(input())
pls=[]
for _ in range(n):
    pls.append([int(x) for x in input().split()])

res=nearestpoints(pls)
for i in res:
    print(*i)
