
t=int(input())
for _ in range(t):
    n,k=[int(x) for x in input().split()]
    p=[int(x) for x in input().split()]

    ans=len(set(range(1,k+1))-set(p[:k]))

    print(ans)




