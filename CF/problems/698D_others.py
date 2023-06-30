

dx=[[0]*(1<<20) for _ in range(20)]
dy=[[0]*(1<<20) for _ in range(20)]
lg=[0]*(1<<20)

def mx(l,r):
    p=lg[r-l+1]
    return max(dx[p][l],dx[p][r-(1<<p)+1])

def mn(l,r):
    p=lg[r-l+1]
    return min(dy[p][l],dy[p][r-(1<<p)+1])


if __name__ == '__main__':
    n=int(input())
    dx[0][1:n]=[int(x) for x in input().split()]
    dy[0][1:n]=[int(x) for x in input().split()]

    for p in range(1,20):
        if (1<<p)>n:
            break
        for i in range(1,n+2-(1<<p)):
            dx[p][i]=max(dx[p-1][i],dx[p-1][i+(1<<(p-1))])
            dy[p][i]=min(dy[p-1][i],dy[p-1][i+(1<<(p-1))])

    for i in range(2,n+1):
        lg[i]=lg[i>>1]+1

    ans=0
    for i in range(1,n+1):
        if mx(i,i)<=mn(i,i):
            l=i-1
            r=i
            p=1<<lg[n-i+1]
            while p:
                if p+l<=n and mx(i,l+p)<mn(i,l+p):l+=p
                if p+r<=n and mx(i,r+p)<=mn(i,r+p):r+=p
                p>>=1

            ans+=r-l

    print(ans)

