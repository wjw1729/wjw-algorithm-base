

t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x  in input().split()]

    unqn=len(set(a))
    if (n-unqn)%2==0:
        print(unqn)
    else:
        print(unqn-1)