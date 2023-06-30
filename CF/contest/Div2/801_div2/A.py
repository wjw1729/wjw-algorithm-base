

t=int(input())
for _ in range(t):
    n,m=[int(x) for x in input().split()]
    mat=[]
    for _ in range(n):
        mat.append([int(x) for x in input().split()])


    maxnum=-float('inf')
    for i in range(n):
        for j in range(m):
            if mat[i][j]>maxnum:
                maxnum=mat[i][j]
                maxi=i
                maxj=j

    h=max(maxi+1,n-maxi)
    w=max(maxj+1,m-maxj)
    print(h*w)


