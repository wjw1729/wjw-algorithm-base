from itertools import product


t=int(input())
for _ in range(t):
    n,m=[int(x) for  x in input().split()]
    mat=[]
    in0=False
    c=0
    for _  in range(n):
        mat.append(input())
        c+=mat[-1].count('1')
        if not in0 and    '0' in mat[-1]:
            in0=True




    check=False
    for i in range(n):
        for j in range(m):
            cnt=0
            for ii,jj in product((i,i+1),(j,j+1)):
                if 0<=ii<n and 0<=jj<m and mat[ii][jj]=='0':
                    cnt+=1
            if cnt>=2:
                check=True
                break
    if check:
        print(c)
    elif in0:
        print(c-1)
    else:
        print(c-2)





