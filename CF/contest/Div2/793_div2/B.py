


t=int(input())
for _ in range(t):

    n=int(input())
    p=[int(x) for x in input().split()]

    ans=None
    for i in range(n):
        if p[i]!=i:
            if ans==None:
                ans=p[i]
            else:
                ans&=p[i]

    print(ans)
