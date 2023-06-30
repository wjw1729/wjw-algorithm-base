from collections import  defaultdict


def getsum(x,y):


    return d1[x-y]+d2[x+y]-mat[x][y]





t=int(input())
for _ in range(t):
    n,m=[int(x) for x  in input().split()]
    mat=[]
    for i in range(n):
        mat.append([int(x) for x in  input().split()])

    d1=defaultdict(int)
    d2=defaultdict(int)

    for i in range(n):
        for j in range(m):
            d1[i-j]+=mat[i][j]
            d2[i+j]+=mat[i][j]


    ans=0
    for i in range(n):
        for j in range(m):
            ans=max(ans,getsum(i,j))

    print(ans)


