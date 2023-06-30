
t=int(input())

for _ in range(t):
    m=int(input())
    a=[]
    a.append([int(x) for  x in input().split()])
    a.append([int(x) for  x in input().split()])

    f=[[0]*m for _ in range(2)]
    q=[[0]*m for _ in range(2)]

    i=0
    j=0
    t=0
    dls=[(1,0),(0,1),(-1,0),(0,1)]
    pt=0
    ans=0
    while j<m:
       f[i][j] = t
       ans=max(ans,t)

       i += dls[pt][0]
       j += dls[pt][1]
       if j>=m:
           break
       t=max(t+1,a[i][j]+1)
       pt+=1
       pt%=4

    #print(f)

    for i in range(1,m):
        q[0][i]=max(q[0][i-1]+1,a[0][i]+1)

    q[1][m-1]=max(q[0][m-1]+1,a[0][m-1]+1)
    for i in range(m-2,-1,-1):
        q[1][i]=max(q[1][i+1]+1,a[1][i]+1)


    #print(q)
    q2=[[0]*m for _ in range(2)]

    q2[1][0]=max(q2[0][0]+1,a[1][0]+1)


    for i in range(1,m):
        q2[1][i]=max(q2[1][i-1]+1,a[1][i]+1)

    q2[0][m-1]=max(q2[1][m-1]+1,a[0][m-1]+1)
    for  i in range(m-2,0,-1):
        q2[0][i]=max(q2[0][i+1]+1,a[0][i]+1)

    ans=min(q[1][0],q2[0][1],ans)

    #print(q2)
    print(ans)




