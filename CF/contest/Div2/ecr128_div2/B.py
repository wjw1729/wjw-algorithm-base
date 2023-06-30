

t=int(input())

for _ in range(t):
    n,m=[int(x) for  x in input().split()]

    matrix=[]
    for _ in range(n):
        matrix.append(input())

    check=True
    sx,sy=-1,-1
    for i in range(n):
        for j in range(m):
            if matrix[i][j]=='R':
                if sx==-1 and sy==-1:
                    sx,sy=i,j
                else:
                    if i<sx or j<sy:
                        check=False
                        break

    if sx==-1 and sy==-1:
        check=False

    if not check:
        print('NO')
    else:
        print('YES')

