

t=int(input())
for _ in range(t):
    n,m,k=[int(x) for x  in input().split()]
    a=[int(x) for x  in input().split()]


    def solve(n,m):

        als=[c//n for c in a if not c//n==1 ]
        if sum(als)<m:
            return False
        als.sort()
        ans=0
        nn=len(als)

        if als[nn-1]>=m:
            return True

        if als[nn-1]==2:
            if m%2==1:
                return False

        for i in range(nn-1,-1,-1):
            if i==nn-1:
                ans=+als[i]-1
            else:
                ans+=als[i]

            if ans>=m-1:
                return True

        return False





    ans=solve(n,m) or solve(m,n)
    if ans:
        print('YES')
    else:
        print('NO')
