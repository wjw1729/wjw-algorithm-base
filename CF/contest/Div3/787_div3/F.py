
def mintime(edges,k):



    return 0
t=int(input())
for _ in range(t):
    n,k=[int(x) for x in input().split()]
    x,y=[int(x) for x in input().split()]
    things=[int(x) for x in input().split()]
    edges=[]
    for _ in range(n-1):
        tmp=[int(x) for x in input().split()]
        edges.append(tmp)

    res=mintime(edges,k)
    print(res)
