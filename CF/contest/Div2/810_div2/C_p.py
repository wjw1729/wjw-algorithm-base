
t=int(input())
for _ in range(t):
    n,m,k=[int(x) for x in input().split()]

    a=[int(x) for  x in input().split()]

    def solve(n,m):
        als=[c//m for c in a if c//m>1]
        if n%2==1 and all(x==2 for x in als):
            return False

        return sum(als)>=n


    if solve(n,m) or solve(m,n):
        print('YES')
    else:
        print('NO')



