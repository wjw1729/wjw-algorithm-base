


t=int(input())
for _ in range(t):
    n,m=[int(x) for  x in input().split()]

    A=[]
    B=[]
    for _ in range(n):
        A.append([int(x) for  x in input().split()])

    for _ in range(n):
        B.append([int(x) for  x in input().split()])



    def solve():
        f=[[0]*(m+1) for _ in range(n)]


        pa=[[0]*(m+1) for _ in range(n)]
        pb=[[0]*(m+1) for _ in range(n)]

        for i in range(n):
            for j in range(1,m+1):
                pa[i][j]=pa[i][j-1]+A[i][j-1]

        for i in range(n):
            for j in range(1,m+1):
                pb[i][j]=pb[i][j-1]+B[i][j-1]

        for i in range(n):
            for j in range(m+1):

                f[i][j]=f[i-1][j]+(pa[i][j]+pb[i][-1]-pb[i][j])
                f[i][j]=max(f[i][j],f[i][j-1])


        return max(f[n-1])

    print(solve())



