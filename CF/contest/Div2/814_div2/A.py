
t=int(input())

for _ in range(t):
    n,m=[int(x) for x in input().split()]

    if (n+m)%2==1:
        print('Burenka')
    else:
        print('Tonya')