
t=int(input())
for _ in range(t):
    n,m=[int(x) for x  in input().split()]

    mat=[[0]*m for _ in range(n)]

    p=[[1,0],[0,1]]

    for i in range(0,n,2):
        if i//2%2==0:
            tmp=p
        else:
            tmp=[p[1],p[0]]
        for j in range(0,m,2):
            mat[i][j:j+2]=tmp[0]
            mat[i+1][j:j+2]=tmp[1]

            tmp=[tmp[1],tmp[0]]

    for a in mat:
        print(*a)


