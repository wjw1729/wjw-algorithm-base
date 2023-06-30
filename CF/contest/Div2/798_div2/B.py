

def solve(p):
    p=[0]+p
    took=[0]*(n+1)
    ans=[]
    for i in range(1,n-1):
        k=1
        while took[k] or k==p[i]:
            k+=1
        ans.append(k)
        took[k]=1

    a=b=-1
    for i in range(1,n+1):
        if not took[i]:
            if a==-1:
                a=i
            else:
                b=i

    if a!=p[n-1] and b!=p[n]:
        ans.append(a)
        ans.append(b)
    else:
        ans.append(b)
        ans.append(a)

    return ans





t=int(input())
for _ in range(t):
    n=int(input())
    p=[int(x) for x  in input().split()]

    if n==1:
        print(-1)
    else:
        res = solve(p)
        print(*res)


