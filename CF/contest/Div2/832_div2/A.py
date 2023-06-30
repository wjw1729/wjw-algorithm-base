t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]

    ans=abs(sum(a))
    print(ans)