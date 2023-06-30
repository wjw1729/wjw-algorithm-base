

t=int(input())
for _ in range(t):
    n,x=[int(x) for x in input().split()]
    h=[int(x) for x in input().split()]
    h.sort()

    ans=all(h[i]<=h[i+n]-x for i in range(n))
    if ans:
        print('YES')
    else:
        print('NO')
