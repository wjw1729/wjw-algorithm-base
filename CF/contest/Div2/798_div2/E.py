

def solve(matrix):

    bls=[]
    lx, rx=n,0
    ly, ry =m,0
    for i in range(n):
        for j in range(m):
            if matrix[i][j]=='B':
                bls.append((i,j))
                lx=min(lx,i)
                rx=max(rx,i)
                ly=min(ly,j)
                ry=max(ry,j)

    def compute(a,b):
        res=0
        for i,j in bls:
            res=max(res,abs(i-a)+abs(j-b))

        return res

    x=(lx+rx)//2
    y=(ly+ry)//2
    ans=float('inf')

    for i in [x-1,x,x+1]:
        for j in [y-1,y,y+1]:
            if compute(i,j)<ans:
                ans=compute(i,j)
                res=(i,j)

    return res







t=int(input())
for _ in range(t):
    n,m=[int(x) for  x in input().split()]
    matrix=[]
    for _ in range(n):
        matrix.append(input())

    res=solve(matrix)

    print(*[x+1 for x  in res])