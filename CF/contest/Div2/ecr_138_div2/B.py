
t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]

    print(sum(a)+sum(b)-max(b))