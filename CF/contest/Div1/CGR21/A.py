

t=int(input())

for _ in range(t):
    n,z=[int(x) for x  in input().split()]
    a=[int(x) for x  in input().split()]

    ans=0
    for c in a:
        ans=max(ans,c|z)

    print(ans)
