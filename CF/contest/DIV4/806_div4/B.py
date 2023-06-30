t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    vis=set()
    ans=0
    for c in s:
        if c in vis:
            ans+=1
        else:
            ans+=2
            vis.add(c)
    print(ans)
