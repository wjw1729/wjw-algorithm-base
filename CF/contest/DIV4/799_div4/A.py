

t=int(input())
for _ in range(t):
    a,b,c,d=[ int(x) for x in input().split()]
    print(sum(x>a for x  in [b,c,d]))