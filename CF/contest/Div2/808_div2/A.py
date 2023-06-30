

t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]

    if all(x%a[0]==0 for x in a[1:]):
        print('YES')
    else:
        print('NO')