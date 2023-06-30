from collections import deque

def elegant(matrix):
    presum=[[0]*(m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            presum[i][j]=presum[i][j-1]+presum[i-1][j]-presum[i-1][j-1]+matrix[i-1][j-1]

    def check(x1,y1,x0,y0):
        tmp=presum[x1+1][y1+1]+presum[x0][y0]-presum[x0][y1+1]-presum[x1+1][y0]
        return tmp==(x1-x0+1)*(y1-y0+1)


    for i in range(n):
        for j in range(m):
            if matrix[i][j]==1:
                q=deque()
                q.append((i,j))

                x0, y0 = n, m
                x1, y1 = 0, 0

                while q:
                    i,j=q.popleft()


                    for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                        if 0<=x<n and 0<=y<m and matrix[x][y]==1:
                            x0=min(x0,x)
                            x1=max(x1,x)
                            y0=min(y0,y)
                            y1=max(y1,y)
                            matrix[x][y]=0
                            q.append((x,y))
                if x0>x1 or y0>y1:
                    continue
                if not check(x1,y1,x0,y0):
                    return False
    return True




t=int(input())

for _ in range(t):
    n,m=[int(x) for  x in input().split()]
    matrix=[]
    for _ in range(n):
        matrix.append([int(x) for x in list(input())])

    res=elegant(matrix)
    if res:
        print('YES')
    else:
        print('NO')