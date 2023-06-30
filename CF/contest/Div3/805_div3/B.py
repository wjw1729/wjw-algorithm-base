t=int(input())
for _ in range(t):
    s=input()
    ans=0
    k=0
    vis=set()
    for c in s:
        if k==0 and c not in vis:
            ans+=1
            k=3
            vis=set()
        if c in vis:
            continue
        else:
            k-=1
            vis.add(c)


    if k==3:
        ans-=1
    print(ans)