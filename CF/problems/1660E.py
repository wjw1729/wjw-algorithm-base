


def minburles(matrix):

    n=len(matrix)

    num1=0

    numd=0
    for j0 in range(n):
        j=j0
        cnt=0
        for i in range(n):
            if matrix[i][j]==1:
                cnt+=1
                num1+=1
            j+=1
            j%=n
        numd=max(numd,cnt)

    return n+num1-2*numd


t=int(input())

for _ in  range(t):
    _=input()
    n=int(input())
    matrix=[]
    for i in range(n):
        matrix.append([int(x) for x in input()])

    print(minburles(matrix))




