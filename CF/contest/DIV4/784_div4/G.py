


def falldown(grid):
    def reverse(grid):
        n=len(grid)
        m=len(grid[0])
        grid=[[grid[i][j] for i in range(n)] for j in range(m)]

        return [''.join(x) for x in grid]

    grid=reverse(grid)
    res=[]
    for g in grid:
        sls=g.split('o')
        tmp=''
        for s in sls:
            a=s.count('*')
            tmp+='.'*(len(s)-a)+'*'*a
            tmp+='o'
        res.append(tmp[:n])

    return reverse(res)


t=int(input())
for _ in range(t):
    n,m=[int(x) for x in input().split()]
    grid=[]
    for _ in range(n):
        grid.append(input())

    res=falldown(grid)
    for c in res:
        print(c)

