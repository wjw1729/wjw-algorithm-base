from collections import defaultdict
def getminpart(parents):

    indeg=[0]*(n+1)
    vis=set()
    for i,c in enumerate(parents):
        if i+1!=c:
            indeg[c]+=1

    leaves=[x for x in range(1,n+1) if indeg[x]==0]

    ans=[]
    for i in leaves:
        path=[i]
        vis.add(i)
        while parents[i-1] not in vis:
            path.append(parents[i-1])
            vis.add(parents[i-1])
            i = parents[i - 1]
        ans.append(path)

    return ans





t=int(input())

for _ in range(t):
    n=int(input())
    parents=[int(x) for x in input().split()]
    res=getminpart(parents)
    print(len(res))
    for v in res:
        print(len(v))
        print(*v[::-1])


